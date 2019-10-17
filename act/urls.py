from django.urls import path

from . import views

urlpatterns = [
    path('add', views.add, name="act-add"), #新增活動
    #path('checkin-select', views.checkinselect, name="act-checkinselect"), #活動簽到選擇
    #path('checkin/<str:id>', views.checkin, name="act-checkin"), #活動簽到
    path('show', views.show, name="act-show"), #活動總覽
]