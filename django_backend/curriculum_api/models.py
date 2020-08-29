from django.db import models

class Curriculum(models.Model):
    name = models.CharField(max_length=30)

class Module(models.Model):
    name = models.CharField(max_length=30)
    module_description = models.CharField(max_length=30)
    curriculum_id = models.IntegerField(default=0)
    
class Submodule_lesson(models.Model):
    name = models.CharField(max_length=30)
    module_id = models.IntegerField(default=0)
    curriculum_id = models.IntegerField(default=0)
    
class Submodule_article(models.Model):
    name = models.CharField(max_length=30)
    module_id = models.IntegerField(default=0)
    curriculum_id = models.IntegerField(default=0)

class Submodule_emulator(models.Model):
    name = models.CharField(max_length=30)
    module_id = models.IntegerField(default=0)
    curriculum_id = models.IntegerField(default=0)

# Create your models here.

