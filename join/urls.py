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
    path('chart', views.chart, name="chart"),
    path('export_all', views.export_all, name="export_all"),
    path('export_NP', views.export_NP, name="export_NP"),
    path('export_M', views.export_M, name="export_M"),
    path('commingsoon', views.commingsoon, name="commingsoon"),
    path('attend', views.attend, name="attend"),
]