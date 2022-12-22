from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('topics/', views.topics_page, name='topics_page'),
    path('activity/', views.activity_page, name='activity_page'),
    path('room/<str:pk>/', views.room_page, name='room_page'),
    path('delete_message/<str:pk>/', views.delete_message_page, name='delete_message_page'),
    path('create_room/', views.create_room_page, name='create_room_page'),
    path('update_room/<str:pk>/', views.update_room_page, name='update_room_page'),
    path('delete_room/<str:pk>/', views.delete_room_page, name='delete_room_page'),
    path('register/', views.register_page, name='register_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('profile/<str:pk>/', views.profile_page, name='profile_page'),
    path('profile_update/', views.update_profile_page, name='update_profile_page'),
]
