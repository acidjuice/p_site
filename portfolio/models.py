from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

class Artwork(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2500)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)