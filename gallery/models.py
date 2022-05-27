from django.db import models

# Create your models here.

class Images(models.Model):
    """
    models to handle images
    """
    image = models.ImageField(upload_to='images/')
    date_posted = models.DateTimeField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=100)
    posted_by = models.CharField(max_length=40, default='admin')


