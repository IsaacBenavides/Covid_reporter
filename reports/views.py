import imp
from django.shortcuts import render
from utils.utils import Utils


def show_reports(request):
    Utils().read_csv()
    return render(request, 'test.html')
