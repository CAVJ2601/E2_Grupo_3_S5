from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length=100, unique=True, primary_key=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
