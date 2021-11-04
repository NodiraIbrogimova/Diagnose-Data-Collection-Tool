from django.urls import path, include
from rest_framework import routers

from src.diagnose import views

diagnose_routers = routers.DefaultRouter()
diagnose_routers.register(r'diagnose', views.DiagnoseViewSet, basename="diagnose")

urlpatterns = [
    path("", include(diagnose_routers.urls))
]
