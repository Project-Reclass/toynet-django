from django.db import models

class ToyNetConfig(models.Model):
    topology = models.TextField(default='<>')
    author_id = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return 'author: ' + str(self.author_id)

class ToyNetSession(models.Model):
    toynetconfig = models.ForeignKey('ToyNetConfig', on_delete=models.CASCADE)
    topology = models.TextField(default='<>')
    user_id = models.IntegerField(blank=True, default=0)
    image = models.TextField(blank=True, default='')
    time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_id) + self.create_time.strftime('%m/%d/%Y, %H:%M:%S')

class ToyNetSessionOperation(models.Model):
    toynet_id = models.ForeignKey('ToyNetSession', on_delete=models.CASCADE)
    action = models.TextField(blank=True, default=0) # make integer?
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.toynet_id + '- ' + self.action + self.time.strftime('%m/%d/%Y, %H:%M:%S')

class ToyNetSessionCommand(models.Model):
    toynet_id = models.ForeignKey('ToyNetSession', on_delete=models.CASCADE)
    host = models.TextField(blank=False)
    command = models.TextField(blank=False) # make integer?
    result = models.TextField(blank=True, default='') # make integer?
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.toynet_id + '- ' + self.host + ':' + self.command + '(' + self.time.strftime('%m/%d/%Y, %H:%M:%S') + ')'
