from django.urls import path

from . import views

app_name = 'course'

urlpatterns = [
    path('show', views.show, name="show"),
]