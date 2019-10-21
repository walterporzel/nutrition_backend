from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=200)
    serving_size = models.DecimalField(max_digits=5, decimal_places=2)
    serving_size_unit = models.CharField(max_length=100)
    calories = models.DecimalField(max_digits=5, decimal_places=2)
    fat = models.DecimalField(max_digits=5, decimal_places=2)
    carbs = models.DecimalField(max_digits=5, decimal_places=2)
    protien = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.name
