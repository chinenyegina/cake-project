from django.db import models

class Special(models.Model):
    name = models.CharField(max_length=255)
    price= models.FloatField()
    image= models.ImageField(upload_to='images/')
    summary= models.TextField()




    def __str__(self):
        return self.name
