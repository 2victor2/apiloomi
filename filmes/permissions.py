from rest_framework import permissions

class FilmePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return request.user.can_create_filme
        elif view.action == 'update':
            return request.user.can_update_filme
        elif view.action == 'delete':
            return request.user.can_delete_filme
        else:
            return True