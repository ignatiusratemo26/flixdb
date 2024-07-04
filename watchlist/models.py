from django.db import models

# Create your models here.
class Watchlist(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    # released or not
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=200)
    website =models.URLField(max_length=90)

    def __str__(self):
        return self.name