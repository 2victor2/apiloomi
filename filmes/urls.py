from django.urls import path
from .views import (
    FilmeListCreateAPIView,
    FilmeDetailAPIView,
    FilmeUpdateAPIView,
    FilmeDestroyAPIView,
)

urlpatterns = [
    path('', FilmeListCreateAPIView.as_view(), name='filme-list-create'),
    path('<int:pk>/', FilmeDetailAPIView.as_view(), name='filme-detail'),
    path('<int:pk>/update/', FilmeUpdateAPIView.as_view(), name='filme-update'),
    path('<int:pk>/delete/', FilmeDestroyAPIView.as_view(), name='filme-destroy'),
    path('filmes/<int:pk>/', FilmeDetailAPIView.as_view(), name='filme-detail'),
]