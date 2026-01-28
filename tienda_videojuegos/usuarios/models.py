from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission




# Create your models here.
class Usuario(AbstractUser):

    email = models.EmailField(unique=True)

    #Evitar conflictos de reverse accessors
    groups = models.ManyToManyField(
        Group,
        related_name="usuario_set", #aqui cambiamos el related_name
        blank=True,
        help_text="Grupos a los que pertenece este usuario.",
        verbose_name="grupos",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="usuario_user_set", #aqui cambiamos el related_name
        blank=True,
        help_text="Permisos específicos para este usuario.",
        verbose_name="permisos de usuario",
    )

    def __str__(self):
        return self.username
    

  