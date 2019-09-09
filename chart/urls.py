from django.urls import path

from . import views

app_name = 'chart'

urlpatterns = [
    path('commingsoondata', views.CommingsoonData.as_view(), name="commingsoondata"),
    path('joinclub', views.joinclub, name="joinclub"),
    path('joinclubdata', views.JoinclubData.as_view(), name="joinclubdata"),
    path('receiveprize', views.receiveprize, name="receiveprize"),
    path('receiveprizedata', views.ReceiveprizeData.as_view(), name="receiveprizedata"),
    path('attendance', views.attendance, name="attendance"),
    path('attendancedata', views.AttendanceData.as_view(), name="attendancedata"),
    path('export_all', views.export_all, name="export_all"),
    path('export_NP', views.export_NP, name="export_NP"),
    path('export_M', views.export_M, name="export_M"),
]