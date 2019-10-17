from django.urls import path

from . import views

urlpatterns = [
    path('add', views.add, name="course-add"), #新增課程
    path('checkin-select', views.checkinselect, name="course-checkinselect"), #課程簽到選擇
    path('checkin/<str:id>', views.checkin, name="course-checkin"), #課程簽到
    path('show', views.show, name="course-show"), #課程總覽
]