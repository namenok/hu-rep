from django.urls import path
from . import views

app_name = 'huapp'

urlpatterns = [
    path('', views.index, name='index'),
]