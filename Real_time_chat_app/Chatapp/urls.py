from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("login",views.login,name='login'),
    path("signup",views.signup,name='signup'),
    # path("chat/<int:pk>/",views.chat,name='chat'),
    path("chat/<str:username>/",views.chat,name='chat'),
    path("user/",views.user,name='user'),
    path("logout/",views.logout,name='logout'),
    path("create_room",views.create_room,name='create_room'),
    path("room/<str:group_name>",views.room,name='room'),
]
