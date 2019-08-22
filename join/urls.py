from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('join', views.join, name="join"),
    path('review', views.review, name="review"),
    path('edit', views.edit, name="edit"),
]