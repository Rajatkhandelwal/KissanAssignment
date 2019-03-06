from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from weather import views

#http://localhost:8000/weather/list?type=Tmax&location=UK&start_date=2016-01-15&end_date=2019-02-25
# http://localhost:8000/weather/getListData?type=Tmax&location=UK&start_date=2016-01-15&end_date=2019-02-25

urlpatterns = [
    path('getListData', views.get),
    path('saveData', views.post)
]
urlpatterns = format_suffix_patterns(urlpatterns)
