from django.shortcuts import render, redirect
from utils.utils import Utils
from .models import CovidRegister
from django.views.generic import TemplateView


class Initial(TemplateView):
    template_name = 'initial.html'
    redirect_url = 'reports:load_data'

class LoadData(TemplateView):
    template_name = 'test.html'

    def get(self, request, *args, **kwargs):
        if(CovidRegister.objects.all().count() == 0):
            Utils().read_csv()
        return render(request, "test.html")
    


