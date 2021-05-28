from django.db import models

# Create your models here.
class User(models.Model):
    user_id     = models.IntegerField(unique=True, primary_key=True)
    first_name  = models.CharField(max_length=64)
    last_name   = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Incoming(models.Model):

    update_id = models.IntegerField(unique=True)
    message = models.TextField(max_length=4000)

    def __str__(self):
        return f'{self.update_id}'