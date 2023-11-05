from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from filmes.models import Filme
from filmes.serializers import FilmeSerializer, LoginSerializer
from rest_framework import generics
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny
from django.shortcuts import render

class LoginView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])

        if user is not None:
            login(request, user)
            return Response({'status': 'success', 'message': 'Login realizado com sucesso'})

        else:
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password'],
            )
            login(request, user)
            return Response({'status': 'success', 'message': 'Conta criada com sucesso'})



@api_view(['POST'])
def api_home(request, *args, **kwargs):
    if request.method == 'POST':
        serializer = FilmeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_filme(request, *args, **kwargs):
    if request.method == 'POST':
        serializer = FilmeSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data.get('titulo')
            content = serializer.validated_data.get('descricao') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        data = request.data
        if User.objects.filter(email=data.get('email')).exists():
            return Response({"error": "E-mail já está em uso."}, status=400)

        user = User.objects.create_user(
            username=data.get('username'),
            password=data.get('password'),
            email=data.get('email')
        )

        return Response({"user_id": user.id}, status=201)