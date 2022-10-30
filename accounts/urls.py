from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('login/', views.login, name='login'),
    path('login/account/', views.account, name='account'),
    path('login/account/return/', views.back_home, name='return'),
    path('login/not_auth/', views.account, name='not_auth'),
    path('login/account/try_again/', views.back_login, name='try_again')
    ]