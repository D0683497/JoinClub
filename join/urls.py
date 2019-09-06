from django.urls import path

from . import views

app_name = 'join'

urlpatterns = [
    path('', views.index, name="index"),
    path('join', views.join, name="join"),
    path('search', views.search, name="search"),
    path('review/<int:id>', views.review, name="review"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('view', views.view, name="view"),
    path('commingsoon', views.commingsoon, name="commingsoon"),
    path('attend', views.attend, name="attend"),
]