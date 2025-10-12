# from django.db import models
# from django.contrib.auth.models import AbstractUser

# # Create your models here.
# class User(AbstractUser):
#     bio = models.TextField(blank=True, null=True)
#     profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
#     followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
#     following = models.ManyToManyField('self', symmetrical=False, related_name='user_following', blank=True)

#     def __str__(self):
#         return self.username

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='user_followers',
        blank=True
    )
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='user_following',
        blank=True
    )

    def __str__(self):
        return self.username
