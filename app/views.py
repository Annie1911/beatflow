from django.shortcuts import render
from django.db import models

# Create your views here.
class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    date_creation = models.DateField(auto_now_add=True)
    # Autres champs ...

    def __str__(self):
        return self.username