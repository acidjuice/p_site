from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    url = models.URLField(blank=True)
    date = models.DateField()