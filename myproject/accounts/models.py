from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    """
    Representa una organización o cliente dentro del sistema SaaS.
    """
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    """
    Extiende el modelo User con datos adicionales.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)
    is_owner = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
