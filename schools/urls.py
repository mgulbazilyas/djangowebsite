from django.urls import path

from . import views

app_name = 'schools'

urlpatterns = [
    path('indexpage/',views.index,name='index'),

]