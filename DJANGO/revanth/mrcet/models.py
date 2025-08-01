from django.db import models

# Create your models here.

class student(models.Model):
     name = models.CharField(max_length=100)
     rollno = models.IntegerField()
     slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
     photo = models.ImageField(upload_to='photos/', null=True)




def __str__(self):
        return f"{self.name}-{self.rollno}"