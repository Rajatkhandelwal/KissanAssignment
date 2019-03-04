from django.contrib import admin

# Register your models here.
from .models import MaxTemperature,MinTemperature,Rainfall

admin.site.register(MinTemperature)
admin.site.register(MaxTemperature)
admin.site.register(Rainfall)
