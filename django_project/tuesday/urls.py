from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home,  name='home'),
    path('login/', views.login, name='login'),

    path('handleLogin/', views.handleLogin, name='handleLogin'),
    path('handelRegister/', views.handelRegister, name='handelRegister'),

    path('register/', views.register, name='register'),
    path('table/', views.table, name='table'),
    path('addnew/', views.addnew, name='addnew'),
    path('addnewdata/', views.addnewdata, name='addnewdata'),
    path('deletedata/<int:user_id>', views.deletedata, name='deletedata'),
    path('edituser/<int:user_id>', views.edituser, name='edituser'),
    path('updatedata/<int:user_id>', views.updatedata, name='updatedata'),

]