from django.urls import path

from . import views

app_name = 'chart'

urlpatterns = [
    path('chart', views.chart, name="chart"),
    path('export_all', views.export_all, name="export_all"),
    path('export_NP', views.export_NP, name="export_NP"),
    path('export_M', views.export_M, name="export_M"),
]