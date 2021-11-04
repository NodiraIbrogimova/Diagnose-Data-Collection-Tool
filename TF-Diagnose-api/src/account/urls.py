from django.urls import path, include
from rest_framework import routers

from src.account import views

user_routers = routers.DefaultRouter()
user_routers.register(r'users', views.UserViewSet, basename="users")

urlpatterns = [

    path("logout/", views.Logout.as_view(), name="logout"),
    path("login/", views.CustomAuthToken.as_view(), name="login"),
    path("", include(user_routers.urls))
]
