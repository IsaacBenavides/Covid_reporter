import datetime
from django.shortcuts import render, redirect
from utils.utils import Utils
from .models import CovidRegister, Location
from django.views.generic import TemplateView, DetailView, ListView
import json


class Initial(TemplateView):
    template_name = 'initial.html'
    redirect_url = 'reports:load_data'

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return redirect(self.redirect_url)


class LoadData(TemplateView):
    def get(self, request, *args, **kwargs):
        if(CovidRegister.objects.all().count() == 0):
            Utils().read_csv()
        return redirect("reports:home")


def home(request):
    all_registers = CovidRegister.objects.all()
    locations = [str(location.location.replace(" ", ""))
                 for location in Location.objects.all()]
    context = {}
    context["locations"] = locations
    for location in locations:
        context[location] = {}
        data = all_registers.filter(location__location=location)
        context[location]["dates"] = json.dumps(
            [date.date.strftime("%d/%m/%Y") for date in data])
        context[location]["total_cases"] = json.dumps(
            [float(total_cases.total_cases) for total_cases in data])
        context[location]["total_deaths"] = json.dumps(
            [float(total_cases.total_deaths) for total_cases in data])
        context[location]["new_cases"] = json.dumps(
            [float(total_cases.new_cases) for total_cases in data])
        context[location]["new_deaths"] = json.dumps(
            [float(total_cases.new_deaths) for total_cases in data])

    return render(request, 'home.html', context)
