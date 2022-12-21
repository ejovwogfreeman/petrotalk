from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    firt_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100, blank=True)
    email = models.EmailField(unique = True)
    bio = models.TextField(null=True)
    image = models.ImageField(null= True, default = 'default.jpg', upload_to='profile_pics')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Topic(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Room(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, unique=True)
    name = models.CharField(max_length = 100)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return self.name

class Message(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, unique=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.body[:50]

