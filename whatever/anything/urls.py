from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name= 'anything'

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.registration, name="register"),
    path('login/', LoginView.as_view(), name="login_url"),

]