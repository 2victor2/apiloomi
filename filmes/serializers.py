from .models import Filme, User
from rest_framework import serializers

class FilmeSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Filme
        fields = [
            "id",
            "usuario",
            "titulo",
            "descricao",
            "link_imagem",
            "data_de_lancamento",
            "diretores",
            "roteiristas",
            "atores",
            "generos",
            "comentarios",
            "estrelas",
            "favorito",
            "status",
        ]

        read_only_fields = ["usuario"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["diretores"] = instance.diretores.split(", ")
        representation["roteiristas"] = instance.roteiristas.split(", ")
        representation["atores"] = instance.atores.split(", ")
        representation["generos"] = instance.generos.split(", ")
        return representation

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
