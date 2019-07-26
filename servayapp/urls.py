from django.urls import path

from servayapp import views

app_name = 'poll_app'


urlpatterns = [
    path('',views.index,name='index'),
    path('polling_page',views.polling,name='polling')
]