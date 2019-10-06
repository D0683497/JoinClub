from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('comingsoon', views.ComingsoonData.as_view(), name="api-comingsoon"),
    path('joinclub', views.JoinclubData.as_view(), name="api-joinclub"),
    path('receiveprize', views.ReceiveprizeData.as_view(), name="api-receiveprize"),
    path('attendance', views.AttendanceData.as_view(), name="api-attendance"),
]