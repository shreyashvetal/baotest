from django.db import models

class UserMerchant(models.Model):
    salt = models.CharField(unique=True, max_length=255)
    is_active = models.BooleanField(default=True)

    def is_authenticated(self):
        return True

class Actor(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    url = models.URLField()

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    actors = models.ManyToManyField(Actor)
