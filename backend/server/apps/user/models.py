import os

from django.contrib.auth.models import AbstractUser
from hashids import Hashids


class User(AbstractUser):
    pass

    @property
    def random_hash_id(self):
        hashids = Hashids(salt=os.environ['SALT'], min_length=5)
        hashed_user_id = hashids.encode(self.id)
        return hashed_user_id
