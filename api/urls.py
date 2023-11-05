from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
  path('login/', views.LoginView.as_view(), name='login'),
  path('auth/', obtain_auth_token),
  path('create-filme/', views.create_filme, name='create-filme'),
  path('register-user/', views.register_user, name='register-user'),
  path('', views.api_home),
]
