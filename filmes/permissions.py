from rest_framework.permissions import BasePermission

from .models import Usuario, Filme


class IsExistingUserPermission(BasePermission):
    def has_permission(self, request, view):
        user_id = view.kwargs.get('user_id')

        if user_id:
            try:
                user = Usuario.objects.get(uuid=user_id)
                request.user = user
                
                return True
            except Usuario.DoesNotExist:

                return False
        else:
            if request.method == 'GET':
                # Allow unauthenticated GET requests
                return True

        return False
    
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Usuario):

            return obj.uuid == request.user.uuid
        elif isinstance(obj, Filme):

            return obj.usuario.uuid == request.user.uuid