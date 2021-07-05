from django.urls import path
from . import views

#app_name= 'register'

urlpatterns = [
    path('register/', views.registration, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]