from django.contrib import admin
from .models import Device, Application, Tipo, deviceApp

admin.site.register(Device)
admin.site.register(Application)
admin.site.register(Tipo)
admin.site.register(deviceApp)
