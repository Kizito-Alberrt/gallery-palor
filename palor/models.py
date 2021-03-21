from django.db import models

# Create your models here.
class Image (models.Models):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
