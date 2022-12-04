
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Infapp
from .forms import NewUserForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, authenticate

def index(request):
  mymembers = Infapp.objects.all().values()
  output = ""
  for x in mymembers:
    output += x["firstname"]
  return HttpResponse(output)

def index(request):
    template = loader.get_template('index.html')
    return render(request, 'index.html')

def landing(request):
    template = loader.get_template('landing.html')
    return render(request, 'landing.html')

def login(request):
    template = loader.get_template('login.html')
    return render(request, 'login.html')

def register(request):
    template = loader.get_template('register.html')
    return render(request, 'register.html')

def saveuser(request):
    form = NewUserForm(request.POST)
    if form.is_valid():
            user = form.save()
            django_login(request, user)      #this line automatically logins the user after registration.
            messages.success(request, "Registration successful.")
            return redirect("/")
    else:
        messages.error(request, form.errors)
    messages.error(
        request, "Unsuccessful registration. Invalid information.")
   
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})
   