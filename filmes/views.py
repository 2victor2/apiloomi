from rest_framework import authentication, generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Filme
from .serializers import FilmeSerializer
from django.shortcuts import get_object_or_404

class FilmeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

class FilmeDetailAPIView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class FilmeUpdateAPIView(generics.UpdateAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    lookup_field = 'pk' 

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title 

class FilmeDestroyAPIView(generics.DestroyAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    lookup_field = 'pk' 

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

@api_view(['GET', 'POST'])
def filme_alt_view(request, pk=None, *args, **kwargs):
    method = request.method  

    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Filme, pk=pk)
            data = FilmeSerializer(obj, many=False).data
            return Response(data)
        # lista d0s filmes
        queryset = Filme.objects.all() 
        data = FilmeSerializer(queryset, many=True).data
        return Response(data)
    
    if method == "POST":
        # postando filme
        serializer = FilmeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('titulo')
            content = serializer.validated_data.get('descricao') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"inválido": "adicione o dado no formato correto"}, status=400)
    

class FilmeMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs): #HTTP -> get
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):

        titulo = serializer.validated_data.get('titulo')
        content = serializer.validated_data.get('descricao') or None
        if content is None:
            content = "Olá!"
        serializer.save(content=content)