from django.db import models

# Create your models here.

class App(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    icon = models.ImageField(upload_to='icons/', default='icons/default_icon.png')
    def __str__(self):
        return self.name

