from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    firt_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100, blank=True)
    email = models.EmailField(unique = True)
    # Bio=models.TextField()
    # image=models.ImageField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    

