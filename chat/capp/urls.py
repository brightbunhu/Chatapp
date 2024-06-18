from django.urls import path
from . import views

urlpatterns =[
    path('home/', views.home, name='home'),
    path('inbox/', views.inbox, name='inbox'),
    #path('chats/', views.inbox, name='chats'),
    path('calls/', views.call, name='calls'),
    path('feedback/', views.feedback, name='feedback'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('kall/', views.kall, name='kall'),
    path('register/', views.register, name='register'),
    path('', views.login, name='login'),
    path('logout/', views.login, name='logout'),
]
