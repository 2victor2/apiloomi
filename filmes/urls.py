from django.urls import path
from .views import (
    FilmeListCreateAPIView,
    FilmeDetailAPIView,
)

urlpatterns = [
    # Path for POST and GET with the path user/<str:user_id>/ (auth)
    path('user/<str:user_id>/', FilmeListCreateAPIView.as_view(), name='filme-list-create'),

    path('<str:uuid>/user/<str:user_id>/', FilmeDetailAPIView.as_view(), name='filme-detail'),
]