from django.urls import path
from . import views

app_name = 'wisesaying'

urlpatterns = [
    path('', views.index, name='index'), 
]
