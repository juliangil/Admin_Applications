from django.shortcuts import render_to_response
from django.http import HttpResponse

def hello(request): #request: Solicitud por convencion y es una instancia de a clase django.http.HttpRequest
    return HttpResponse("Hello world")

def inicio(request):
    return render_to_response('inicio.html')