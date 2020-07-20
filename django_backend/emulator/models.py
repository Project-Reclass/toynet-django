from django.db import models

class MiniNet(models.Model):
    networkConfig = models.CharField(max_length=30)
# Create your models here.
