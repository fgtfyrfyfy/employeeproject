from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(max_length=200)
    salary = models.IntegerField(max_length=200)
    position = models.CharField(max_length=200)

    def __str__(self):
        return self.name