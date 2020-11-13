from django.contrib import admin
from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
    path("", views.index, name="index"),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('dashboard/user_detail/<int:pk>', views.UserDetailView.as_view(), name='user_detail'),
    path('dashboard/user_update/<int:pk>', views.UserUpdateView.as_view(), name='user_update'),
]
