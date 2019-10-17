from django.urls import path

from . import views

urlpatterns = [
    path('form', views.form, name="tea-form"), #事前調查表單
    path('checkin', views.checkin, name="tea-checkin"), #簽到
    path('prize/<str:nid>', views.prize, name="tea-prize"), #領獎
    path('show', views.show, name="tea-show"), #總覽
    path('search', views.search, name="tea-search"), #搜尋
    path('view/<str:nid>', views.view, name="tea-view"), #單筆
    path('edit/<str:nid>', views.edit, name="tea-edit"), #編輯
    path('delete/<str:nid>', views.delete, name="tea-delete"), #刪除
]