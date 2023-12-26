from django.db import models

# Create your models here.
class Movie(models.Model):
    image= models.ImageField(upload_to='imgs')
    name= models.CharField(max_length=100)
    year= models.IntegerField()
    desc= models.TextField()

    def __str__(self):
        return self.name