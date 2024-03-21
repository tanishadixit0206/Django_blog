from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
    
# class UserManager(BaseUserManager):
#     use_in_migrations=True
#     def create_user(self, username, password=None):
#         if not username:
#             raise ValueError('Users must have a username')

#         user = self.model(
#             username=username,
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password):
#         user = self.create_user(
#             username=username,
#             password=password,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.save(using=self._db)
#         return user

#     def get_by_natural_key(self, username):
#         return self.get(username=username)
    
# class User(AbstractBaseUser):
#     username = models.CharField(max_length=100,unique=True)
#     password = models.CharField(max_length=100)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff=models.BooleanField(default=False)
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []
#     # objects = BaseUserManager()
#     def __str__(self):
#         return self.username