from django.contrib import admin
from django.urls import path,include
from  userde import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),

    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('signupUser/', views.signupUser, name='signupUser')


]

