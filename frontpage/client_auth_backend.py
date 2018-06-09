from django.contrib.auth.hashers import check_password

from .models import Clients

class ClientAuthBackend:

    def authenticate(self, request, username=None, password=None):
        try:
            user = Clients.objects.get(login=username)
        except Clients.DoesNotExist:
            return None
        if not user:
            return None
        pwd_valid = check_password(password, user.userpass)
        if pwd_valid:
            return user
        return None

    def get_user(self, user_id):
        try:
            return Clients.objects.get(pk=user_id)
        except Clients.DoesNotExist:
            return None