from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from . import views

urlpatterns = [
  path('login/', views.LoginView.as_view(), name='login'),
  # path('create-filme/', views.create_filme, name='create-filme'),
  # path('register-user/', views.register_user, name='register-user'),
  # path('api/', views.api_home),
  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
  path('api/docs/', SpectacularSwaggerView.as_view(), name='docs'),

]

