from django.db import models

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=80, unique=True)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
