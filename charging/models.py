from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    slots = models.IntegerField()
    rate = models.FloatField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    units = models.FloatField()
    total_cost = models.FloatField()

    def __str__(self):
        return self.customer_name