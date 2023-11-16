from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission, User
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

import uuid
import unicodedata


class UserManager(BaseUserManager):
    def normalize_username(cls, username):
        return (
            unicodedata.normalize("NFKC", username)
            if isinstance(username, str)
            else username
        )

    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('O username é obrigatório')
        username = self.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)

        # Username único
        if Usuario.objects.exclude(pk=user.pk).filter(username=user.username).exists():
            raise ValidationError('Este username já está em uso.')

        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=255, unique=True, blank=True, null=True)
    nome = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    imagem_perfil = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    can_create_filme = models.BooleanField(default=False)
    can_update_filme = models.BooleanField(default=False)
    can_delete_filme = models.BooleanField(default=False)


    groups = models.ManyToManyField(Group, related_name='usuarios')
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios_permissions')

    def __str__(self):
        return self.username or 'User #%s' % self.pk


class Filme(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
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

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='filmes')

    class Meta:
        ordering = ['titulo']

    @property
    def criador(self):
        return self.usuario

