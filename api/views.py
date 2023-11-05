from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from filmes.serializers import FilmeSerializer, LoginSerializer
from rest_framework import generics
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

class LoginView(generics.CreateAPIView):
  permission_classes = [permissions.AllowAny]
  serializer_class = LoginSerializer

  def post(self, request, *args, **kwargs):
    form = AuthenticationForm(request, data=request.data)

    if form.is_valid():
      user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

      if user is not None:
        login(request, user)
        return Response({'status': 'success', 'message': 'Login realizado com sucesso'})

    return Response({'status': 'error', 'message': 'Usuário ou senha inválidos'})

def login_api(request):
  username = request.data.get('username')
  password = request.data.get('password')

  user = authenticate(username=username, password=password)
  if user is not None:
    login(request, user)
    return Response({'status': 'success', 'message': 'Login realizado com sucesso'})
  else:
    return Response({'status': 'error', 'message': 'Usuário ou senha inválidos'})



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