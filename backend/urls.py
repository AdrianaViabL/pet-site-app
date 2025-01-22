from os import path
from django.urls import include

INSTALLED_APPS = [
    'rest_framework',
]

urlpatterns = [
    path('api-auth/', include('rest_framework.urls'))
]