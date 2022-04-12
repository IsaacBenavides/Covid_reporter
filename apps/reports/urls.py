from django.urls import path
from .views import initial, load_data

app_name = 'reports'

urlpatterns = [
    path('', initial, name='initial'),
    path('home/', load_data, name='load_data'),

]
