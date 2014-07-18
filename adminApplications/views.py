from django.shortcuts import render_to_response
from django.http import HttpResponse

def hello(request): #request: Solicitud por convencion y es una instancia de a clase django.http.HttpRequest
    return HttpResponse("Hello world")

def login(request):
    return render_to_response('login.html')

def inicio(request):
    return render_to_response('inicio.html')

def register(request):
    return render_to_response('register.html')

def newDevice(request):
    return render_to_response('newDevice.html')

def newApplication(request):
    return render_to_response('newApplication.html')

def allDevices(request):
    return render_to_response('allDevices.html')

def allApplications(request):
    return render_to_response('allApplications.html')

def oneDevice(request):
    return render_to_response('oneDevice.html')

def oneApplication(request):
    return render_to_response('oneApplication.html')

def installApplications(request):
    return render_to_response('installApplications.html')

def deviceDetails(request):
    return render_to_response('deviceDetails.html')

def applicationDetails(request):
    return render_to_response('applicationDetails.html')