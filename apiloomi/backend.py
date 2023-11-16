from django.contrib.auth.backends import BaseBackend
from filmes.models import Usuario # Import your custom user model

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            return None  # Return None if the user doesn't exist

        if user.check_password(password):
            return user  # Return the user object if the password is valid
        else:
            return None  # Return None if the password is invalid

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None