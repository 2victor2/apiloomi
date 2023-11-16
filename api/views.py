from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

from filmes.models import Filme, Usuario
from filmes.serializers import LoginSerializer, UsuarioSerializer


class LoginView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])

        if user is not None:
            login(request, user)
            return Response({'user_id': UsuarioSerializer(user).data['uuid']})

        else:
            try:
                Usuario.objects.get(username=serializer.validated_data['username'])

                return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_400_BAD_REQUEST)
            except Usuario.DoesNotExist:
                user = Usuario.objects.create_user(
                    username=serializer.validated_data['username'],
                    password=serializer.validated_data['password'],
                )
                login(request, user)
                return Response({'user_id': UsuarioSerializer(user).data['uuid']}, status=status.HTTP_201_CREATED)

LoginView.csrf_exempt = True