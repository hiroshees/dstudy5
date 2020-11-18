from django.contrib import admin
from django.urls import path

from . import views

app_name = "enkai"

urlpatterns = [
    path("dashboard/category/list", views.CategoryListView.as_view() , name="category_list"),
    path('dashboard/category/create', views.CategoryCreateView.as_view(), name='category_create'),
    path('dashboard/category/edit/<int:pk>', views.CategoryEditView.as_view(), name='category_edit'),
    path("dashboard/event/list", views.EventListView.as_view() , name="event_list"),
    path('dashboard/event/create', views.EventCreateView.as_view(), name='event_create'),
    path('dashboard/event/edit/<int:pk>', views.EventEditView.as_view(), name='event_edit'),
    path("dashboard/event/mylist", views.MyOwnerEventView.as_view() , name="event_mylist"),
    path("dashboard/event/detail/<int:pk>", views.EventDetailView.as_view() , name="event_detail"),
    path("dashboard/event_user/create/<int:event_id>", views.EventUserCreateView.as_view() , name="event_user_create"),
    path("dashboard/event_user/delete/<int:event_id>", views.EventUserDeleteView.as_view() , name="event_user_delete"),
    path("dashboard/chat/<int:event_id>", views.ChatCreateView.as_view() , name="chat"),
]
