from django.urls import path
from .views import RegisterView,ProfileView,UserListView,ChatHistoryView,SendMessageView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',obtain_auth_token,name='login'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('users/',UserListView.as_view(),name='user-list'),
    path('chat/<int:user_id>/',ChatHistoryView.as_view(),name='chat-history'),
    path('message/send/',SendMessageView.as_view(),name='send-message')


]