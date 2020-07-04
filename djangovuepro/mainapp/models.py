from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    images = models.ImageField(upload_to='mainapp/static/original/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title