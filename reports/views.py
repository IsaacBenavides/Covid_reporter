import imp
from django.shortcuts import render
from .models import CovidRegister


def show_reports(request):
    return render(request, 'test.html')
