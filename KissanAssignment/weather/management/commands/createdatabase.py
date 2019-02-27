# Python imports
import requests
from requests.exceptions import RequestException

# Django imports
from django.core.management.base import BaseCommand
from weather.regionConstant import *

locations = [ENGLAND,SCOTLAND,UK,WALES]

class Command(BaseCommand):
    help = "Fetches data from the S3 urls and writes it to database via the API"
    base_url = "https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice"
    host = "localhost:8000"

    def handle(self, *args, **kwargs):
        metoffice_data = {}
        host = "http://%s" % self.host
        self.stdout.write("It's now (%s)" % (host))

        for location in locations:
            metoffice_data[location] = {}
            self.stdout.write("Location: %s, creating Tmax records ..." % location)
            # Create MaxTemperature records
            try:
                url = "%s/Tmax-%s.json" % (self.base_url, location)
                try:
                    resp = requests.get(url)
                    resp.raise_for_status()
                    resp_json = resp.json()
                    metoffice_data[location]["tmax"] = resp_json
                    body = {"type": "Tmax", "location": location, "data": resp_json}
                    requests.post("%s/weather/saveData" % host, json=body)
                except RequestException as exc:
                    raise exc
            except Exception as exc:
                self.stderr.write(exc.__str__())

            self.stdout.write("Location: %s, creating Tmin records ..." % location)
            # Create MinTemperature records
            try:
                url = "%s/Tmin-%s.json" % (self.base_url, location)
                try:
                    resp = requests.get(url)
                    resp.raise_for_status()
                    resp_json = resp.json()
                    metoffice_data[location]["tmin"] = resp_json
                    body = {"type": "Tmin", "location": location, "data": resp_json}
                    requests.post("%s/weather/saveData" % host, json=body)
                except RequestException as exc:
                    raise exc
            except Exception as exc:
                self.stderr.write(exc.__str__())

            self.stdout.write("Location: %s, creating Rainfall records ..." % location)
            # Create Rainfall records
            try:
                url = "%s/Rainfall-%s.json" % (self.base_url, location)
                try:
                    resp = requests.get(url)
                    resp.raise_for_status()
                    resp_json = resp.json()
                    metoffice_data[location]["rainfall"] = resp_json
                    body = {"type": "Rainfall", "location": location, "data": resp_json}
                    requests.post("%s/weather/saveData" % host, json=body)
                except RequestException as exc:
                    raise exc
            except Exception as exc:
                self.stderr.write(exc.__str__())