from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    nom = models.CharField(max_length=255, null=True)
    type_Admin = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='admin_images/',default='defoultpic.png' )

