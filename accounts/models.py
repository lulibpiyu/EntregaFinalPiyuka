from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    #fecha_nacimiento = models.DateField()fecha_nacimiento
    email = models.EmailField(unique=True)
    #is_staff = models.BooleanField(default=False)
    #is_superuser = models.BooleanField(default=False)
    #is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombre', 'apellido']
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username