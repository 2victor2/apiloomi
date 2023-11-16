from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Filme
from .permissions import IsExistingUserPermission
from .serializers import FilmeSerializer


class FilmeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    permission_classes = [IsExistingUserPermission]
    detail=False

    def get_queryset(self):
        filters = Q()

        # Check if user_id is present in URL parameters
        user_id = self.kwargs.get('user_id')

        if user_id:
            # Case: 'user/<str:user_id>/' path
            filters &= Q(usuario__uuid=user_id)

        return self.queryset.filter(filters).select_related("usuario")
    
    def create(self, request, *args, **kwargs):
        data = self.request.data.copy()
        data["usuario"] = self.request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class FilmeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    permission_classes = [IsExistingUserPermission]
    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"
