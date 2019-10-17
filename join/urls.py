from django.urls import path

from . import views

urlpatterns = [
    path('form', views.form, name="join-form"), #入社表單
    path('search', views.search, name="join-search"), #入社表單
    path('view/<str:nid>', views.view, name="join-view"), #單筆
    path('review/<str:nid>', views.review, name="join-review"), #審核
    path('show', views.show, name="join-show"), #總覽
    path('edit/<str:nid>', views.edit, name="join-edit"), #編輯
]