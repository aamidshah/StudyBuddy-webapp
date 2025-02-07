# from django.db import models
# from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#   name = models.CharField(max_length=200,null=True)
#   email = models.EmailField(null=True,unique=True)
#   bio = models.TextField(null=True)
 

#   avatar = models.ImageField(null=True, default="avatar.svg")

#   USERNAME_FIELD= 'email'
#   REQUIRED_FIELDS = []
    


# class Topic(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

# class Room(models.Model):
#     host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
#     name = models.CharField(max_length=200)
#     description = models.TextField(null=True, blank=True)
#     participants = models.ManyToManyField(User, related_name='participants',blank=True)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)


#     class Meta:
#         ordering = ['-updated', 'created']

#     def __str__(self):
#         return self.name

# class Message(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     body = models.TextField()
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.body[0:50]

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(unique=True)  # Removed null=True (email should always exist)
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Added username so superuser creation works

    def __str__(self):
        return self.name if self.name else self.email  # Show email if name is missing


class Topic(models.Model):
    name = models.CharField(max_length=200, unique=True)  # Added unique constraint

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', 'created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']  # Ensures latest messages come first

    def __str__(self):
        return self.body[:50]  # Trims long messages
