from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    age = models.IntegerField(null=True,blank=True)
    movie = models.ForeignKey("Movie", on_delete = models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name + "," + self.city

class Movie(models.Model):
    name = models.CharField(max_length=40)
    avail = models.IntegerField()

    def __str__(self):
        return self.name