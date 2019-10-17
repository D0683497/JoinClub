from django.urls import path

from . import views

urlpatterns = [
    path('teacher', views.teacher, name="add-teacher"), #新增講師
    path('location', views.location, name="add-location"), #新增地點
    path('category', views.category, name="add-category"), #新增類別
    path('lesson', views.lesson, name="add-lesson"), #新增系級
    path('attendee', views.attendee, name="add-attendee"), #新增系級
]