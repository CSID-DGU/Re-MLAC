from django.urls import path
from . import views

urlpatterns = [
    path('/analysis', views.analysis_packet, name="analysis_packet"),
]