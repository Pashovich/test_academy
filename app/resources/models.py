from django.db import models


class Resources(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length= 20)
    amount = models.IntegerField()
    unit = models.CharField(max_length= 5)
    price = models.IntegerField()
    cost = models.IntegerField()
    date = models.DateField()
