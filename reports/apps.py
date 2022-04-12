from django.apps import AppConfig
import os


class ReportsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reports'

    # def ready(self):
    #     run_once = os.environ.get('CMDLINERUNNER_RUN_ONCE')
    #     if run_once is not None:
    #         return
    #     os.environ['CMDLINERUNNER_RUN_ONCE'] = 'True'
    #     from utils.utils import Utils
    #     from .models import CovidRegister

    #     if CovidRegister.objects.all().count() == 0:
    #         Utils().read_csv()
