from django.contrib.auth.backends import ModelBackend
from django.conf import settings
from django.contrib.auth.models import User

class customAuth:
    def authenticate(self, request, username=None):
        try:
            user = User.objects.get(username=username)
            return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None