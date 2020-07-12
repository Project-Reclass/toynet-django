from django.db import models

class Picture(models.Model):
    upload = models.FileField(upload_to='uploads/')
# Create your models here.
