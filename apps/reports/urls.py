from django.urls import path
from .views import home, Initial, LoadData

app_name = 'reports'

urlpatterns = [
    path('', Initial.as_view(), name='initial'),
    path('load_data/', LoadData.as_view(), name='load_data'),
    path('home/', home, name='home'),
]
