from django.urls import path
from . import views

app_name = 'huapp'

urlpatterns = [
    path('', views.index, name='index'),  # /first
    path('home', views.home, name='home'),
    path('checkme', views.checkme, name='checkme'),
    path('library', views.library, name='library'),
    path('calendar', views.calendar, name='calendar'),
    path('test_form', views.test_form, name='test_form'),

]
