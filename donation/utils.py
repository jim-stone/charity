from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User


class EmailLoginBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        print('authenticating...')
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            return user
        except User.DoesNotExist:
            return None
        