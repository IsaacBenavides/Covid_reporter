from django.urls import path
from .views import show_reports
app_name = 'reports'


urlpatterns = [
    path('', show_reports, name='reports'),
]
