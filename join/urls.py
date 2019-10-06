from django.urls import path

from . import views

app_name = 'join'

urlpatterns = [
    path('form', views.form, name="join-form"),
    path('search', views.search, name="join-search"),
    path('review/<int:id>', views.review, name="join-review"),
    path('edit/<int:id>', views.edit, name="join-edit"),
    path('view', views.view, name="join-view"),
]