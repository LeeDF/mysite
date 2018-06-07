from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255)
    cdate = models.DateTimeField()
    pwd = models.CharField(max_length=255)
    age = models.IntegerField()
    sex = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.username
