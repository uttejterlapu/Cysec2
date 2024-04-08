from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Mapping the empty path to the index view
    path('signup/', views.signup_main, name='signup'),
    path('login/', views.login_main, name='login'),
    path('logout/', views.logout_main, name='logout'),
    path('projectc/', views.create_project, name='projectc'),  # Mapping project creation URL
]