from django.db import models

class Soildata(models.Model):
    ec = models.IntegerField()
    ph = models.IntegerField()
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type
