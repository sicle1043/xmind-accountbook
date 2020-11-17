from django.db import models


# Create your models here.
class Record(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(null=False)
    type = models.IntegerField(null=False)
    category = models.CharField(max_length=100)
    amount = models.FloatField(null=False)


class Category(models.Model):
    id = models.CharField(null=False, primary_key=True, max_length=50)
    name = models.CharField(null=False, max_length=100)
    type = models.IntegerField(null=False, )
