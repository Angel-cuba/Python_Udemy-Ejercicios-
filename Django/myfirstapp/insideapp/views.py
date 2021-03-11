from django.shortcuts import render
# from django.http import HttpResponse
from .models import Person


# Create your views here.
def index(request):
     return render(request, "insideapp/base.html", {"personas: ":Person.objects.all()})


def saludos(request):
     return render(request, "insideapp/saludos.html")