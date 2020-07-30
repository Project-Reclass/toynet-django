from django.db import models

class MininetInstance(models.Model):
    networkconfig = models.TextField(default='<>')
    user = models.IntegerField(blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + self.created.strftime('%m/%d/%Y, %H:%M:%S')
