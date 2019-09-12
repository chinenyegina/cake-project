from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=255)
    price= models.FloatField()
    image= models.ImageField(upload_to='images/')
    summary= models.TextField()

class Cake(models.Model):
    name = models.CharField(max_length=255)
    price= models.FloatField()
    image= models.ImageField(upload_to='images/')
    summary= models.TextField()


class CupCake(models.Model):
    name = models.CharField(max_length=255)
    price= models.FloatField()
    image= models.ImageField(upload_to='images/')
    summary= models.TextField()

class Cookies(models.Model):
    name = models.CharField(max_length=255)
    price= models.FloatField()
    image= models.ImageField(upload_to='images/')
    summary= models.TextField()

class Treats(models.Model):
    name = models.CharField(max_length=255)
    price= models.FloatField()
    image= models.ImageField(upload_to='images/')
    summary= models.TextField()

    def __str__(self):
        return self.name
