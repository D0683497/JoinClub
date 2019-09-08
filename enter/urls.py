from django.urls import path

from . import views

app_name = 'enter'

urlpatterns = [
    path('attend', views.attend, name="attend"),
    path('attendsearch', views.attendsearch, name="attendsearch"),
]