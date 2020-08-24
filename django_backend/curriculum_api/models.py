from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=30)
    
class Submodule(models.Model):
    name = models.CharField(max_length=30)
    

# Create your models here.
