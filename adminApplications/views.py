from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.context import RequestContext

from django import forms
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from forms import SignUpForm

def hello(request): #request: Solicitud por convencion y es una instancia de a clase django.http.HttpRequest
    return HttpResponse("Hello world") 

def principal(request):
    return render_to_response('principal.html', {}, context_instance=RequestContext(request))
 
def nuevoUsuario(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # Mira si todas las reglas de validacion pasan
 
            # Borra las variables del formulario forms.py
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
 
            # Crea uns usuario en la base de datos con los datos que le 
            # pasemos
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
 
            # Guarda en la base de datos
            user.save()
 
            return HttpResponseRedirect(reverse('principal'))  
            # Retornda despues del post, pero como esta en nuevoUsuario, el reverse
            # hace que retorne a la pagina anterior en este caso principal

    else:
        form = SignUpForm()
 
    formulario = {'form': form,}
    return render_to_response('login2.html', formulario, context_instance=RequestContext(request))


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