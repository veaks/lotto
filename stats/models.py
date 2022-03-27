from django.db import models

class Draws(models.Model):
    number = models.IntegerField(primary_key=True)
    n1 = models.IntegerField(null=True, blank=True)
    n2 = models.IntegerField(null=True, blank=True)
    n3 = models.IntegerField(null=True, blank=True)
    n4 = models.IntegerField(null=True, blank=True)
    n5 = models.IntegerField(null=True, blank=True)
    n6 = models.IntegerField(null=True, blank=True)
    n7 = models.IntegerField(null=True, blank=True)
    n8 = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-number']
