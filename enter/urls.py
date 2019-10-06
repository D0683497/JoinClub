from django.urls import path

from . import views

app_name = 'enter'

urlpatterns = [
    path('attend', views.attend, name="enter-attend"),
    path('search', views.search, name="enter-search"),
    path('edit/<int:id>', views.edit, name="enter-edit"),
    path('checkin', views.checkin, name="enter-checkin"),
    path('prize/<str:nid>', views.prize, name="enter-prize"),
]