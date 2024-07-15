from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('login/', auth_views.LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('join_event/', views.join_event, name='join_event'),
    path('events/', views.events_page, name='events_page'),
    path('register/', views.register, name='register'),
]
