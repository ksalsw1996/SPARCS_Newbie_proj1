from django.db import models

class UsrContext(models.Model):
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    pato = models.IntegerField()
    phone = models.CharField(max_length=20)

class team(models.Model):
    kingname = models.CharField(max_length=20)
    kinguser = models.CharField(max_length=20)
    kingpato = models.IntegerField()
    kingphone = models.CharField(max_length=20, default='00000000000')
    slaves = models.ManyToManyField('UsrContext')
    startT = models.CharField(max_length=20, default='00:00')
    destination = models.CharField(max_length=20, default='station')
    established = models.BooleanField(default=False)
# Create your models here.
