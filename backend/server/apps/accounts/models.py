import random
import string

from django.contrib.auth.models import User
from django.db import models
from django.http import JsonResponse


class AwsickUser(models.Model):
    """ A Wrapper around the base django user model.
    """
    # Created during account creation
    date_created = models.DateTimeField(auto_now_add=True)
    uuid = models.CharField(max_length=64, db_index=True, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)


def create_new_user(username, password):
    # TODO(allen): Check to see if a user with this username exists already
    # TODO(allen): Check to see if the password sucks
    new_user = AwsickUser(
        uuid=_get_random_app_user_id(),
        user=User.objects.create_user(username, None, password))
    new_user.save()
    return JsonResponse({})


def _get_random_app_user_id():
    """ Generate a random string and verify that it's unique
    """
    random_str = None
    while random_str is None or AwsickUser.objects.filter(uuid=random_str).exists():
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        random_str = ''.join([random.choice(chars) for char in range(15)])
    return random_str
