from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.models import Group, Permission



# Create your models here.


# class User(AbstractUser):
#     groups = models.ForeignKey(
#         Group,
#         related_name='account_users',
#         on_delete=models.CASCADE,
#     )

#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name='account_users',
#         on_delete=models.CASCADE,
#     )


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    groups = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='account_users',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='account_users',
       )