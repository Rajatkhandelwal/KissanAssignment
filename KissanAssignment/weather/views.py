import _thread

from django.db import transaction
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from .models import MaxTemperature,MinTemperature,Rainfall
from .serializers import MaxTempSerializer,MinTempSerializer,RainfallSerializer
from .regionConstant import *

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

valid_types = ("Tmax", "Tmin", "Rainfall")
locations = (ENGLAND,SCOTLAND,UK,WALES)

def run_in_thread(func):
    def function_wrapper(*args):
        _thread.start_new_thread(func, (*args,))
    return function_wrapper


@csrf_exempt
def get(request):
    if request.method == 'GET':
        try:
            body = request.GET.dict()
            metric_type = body.get("type", None)
            start_date = body.get("start_date", "")
            end_date = body.get("end_date", "")
            location = body.get("location",None)

            start_dt = ""
            end_dt = ""

            if start_date:
                try:
                    start_dt = timezone.datetime.strptime(start_date, "%Y-%m-%d")
                except Exception:
                    raise Exception("Invalid start date format")

            if end_date:
                try:
                    end_dt = timezone.datetime.strptime(end_date, "%Y-%m-%d")
                except Exception:
                    raise Exception("Invalid end date format")

            if start_dt and end_dt and start_dt > end_dt:
                return DataException("Start date can't be greater than end date")

            if metric_type not in valid_types or location not in locations:
                return DataException("Please provide metric type and location within range")

            kwargs = {"region": location}
            if start_date:
                kwargs.update({"record_date__gte": start_dt})
            if end_date:
                kwargs.update({"record_date__lte": end_dt})

            if metric_type == "Tmax":
                results = MaxTempSerializer(MaxTemperature.objects.filter(**kwargs), many=True).data
            elif metric_type == "Tmin":
                results = MinTempSerializer(MinTemperature.objects.filter(**kwargs), many=True).data
            elif metric_type == "Rainfall":
                results = RainfallSerializer(Rainfall.objects.filter(**kwargs), many=True).data

            resp = []
            for temp in results:
                tempObject = {}
                convertDate = str(temp["year"]) + "-" + str(temp["month"])
                tempObject[convertDate] = temp["value"]
                resp.append(tempObject)
            return JSONResponse(resp,status=status.HTTP_200_OK)
        except Exception as exc:
            return JSONResponse({"status": "error","message":exc },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JSONResponse({"status": "error", "message": "%s method not allowed" %(request.method)},
                        status=status.HTTP_403_FORBIDDEN)


@csrf_exempt
@run_in_thread
@transaction.atomic
def post(request):
    body = JSONParser().parse(request)
    try:
        metric_type = body.get("type", None)
        location = body.get("location", None)
        array = body.get("data", "")

        if metric_type not in valid_types or location not in locations:
            DataException("Please provide metric type and location within range")

        if metric_type == "Tmax":
            database = MaxTemperature
        elif metric_type == "Tmin":
            database = MinTemperature
        elif metric_type == "Rainfall":
            database = Rainfall
        for record in array:
            database.objects.add_or_update_record(record["value"], location, record["month"], record["year"])
        return JsonResponse({"status": "success", "results": True}, status=status.HTTP_201_CREATED)
    except Exception as exc:
        return JsonResponse({"status": "error","message":exc}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def DataException(message):
    return JsonResponse({"status": "failed", "results": message},status=status.HTTP_400_BAD_REQUEST)

