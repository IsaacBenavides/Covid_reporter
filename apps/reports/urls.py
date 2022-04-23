from django.urls import path
from .views import Initial, LoadData

app_name = 'reports'

urlpatterns = [
    path('', Initial.as_view(), name='initial'),
    path('home/', LoadData.as_view(), name='load_data'),
]
