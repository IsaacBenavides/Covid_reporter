from django.shortcuts import render, redirect
from utils.utils import Utils
from .models import CovidRegister


def initial(request):
    if(CovidRegister.objects.all().count() == 0):
        return render(request, 'initial.html')
    else:
        return redirect('/home/')


def load_data(request):
    if(CovidRegister.objects.all().count() == 0):
        Utils().read_csv()
    return render(request, 'test.html')
