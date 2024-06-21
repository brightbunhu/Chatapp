from django.urls import path
from . import views

urlpatterns =[
    path('home/<int:pk>/', views.home, name='home'),
    path('inbox/<str:pk>/', views.inbox, name='inbox'),
    path('send_message/<str:recipient_id>/', views.send_message, name='send_message'),
    #path('chats/', views.inbox, name='chats'),
    path('calls/<str:pk>/', views.call, name='calls'),
    path('feedback/', views.feedback, name='feedback'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('kall/', views.kall, name='kall'),
    path('register/', views.register, name='register'),
    path('', views.login, name='login'),
    path('logout/', views.login, name='logout'),
]
