from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission, User
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O Email é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        # Email único
        if User.objects.exclude(pk=user.pk).filter(email=user.email).exists():
            raise ValidationError('Este email já está em uso.')

        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=True, null=True)
    nome = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    imagem_perfil = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    # Adicione o campo de senha com um valor padrão seguro
    password = models.CharField(max_length=128, default=make_password('temporary_password'))

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    groups = models.ManyToManyField(Group, related_name='usuarios')
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios_permissions')

    def __str__(self):
        return self.email


class Filme(models.Model):
    titulo = models.CharField(max_length=120)
    descricao = models.TextField(max_length=1200, blank=True, null=True)
    link_imagem = models.CharField(max_length=255, blank=True, null=True)
    data_de_lancamento = models.DateField(blank=True, null=True)
    comentarios = models.TextField(blank=True, null=True)
    estrelas = models.FloatField(null=True, blank=True)
    favorito = models.BooleanField(default=False)
    status = models.CharField(max_length=255, blank=True, null=True)
    diretores = models.CharField(max_length=320, blank=True, null=True, default="")
    roteiristas = models.CharField(max_length=320, blank=True, null=True, default="")
    atores = models.CharField(max_length=320, blank=True, null=True, default="")
    generos = models.CharField(max_length=320, blank=True, null=True, default="")

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['titulo']

    @property
    def criador(self):
        return self.usuario

