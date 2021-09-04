from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    url = models.URLField(blank=True)
    date = models.DateField()

    def __str__(self): #show NAME in Admin page instead of table ID
        return self.title