from django.db import models

class Url(models.Model):
    key=models.CharField(primary_key=True,null=False,max_length=16)
    long_url=models.CharField(null=False,max_length=272)
    short_url=models.CharField(null=False,max_length=256)
    