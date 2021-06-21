from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class Pizza(models.Model):

    def __str__(self):
        return self.name
    

    TYPE_CHOICES = (
        ('Regular', 'Regular'),
        ('Square', 'Square'),
    )
    
    SIZE_CHOICES = (
        ('Small','Small'),
        ('Medium','Medium'),
        ('Large','Large'),
    )

    TOPPINGS_CHOICES = (
        ('Onion', 'Onion'),
        ('Tomato', 'Tomato'),
        ('Capsicum', 'Capsicum'),
        ('Corn', 'Corn'),
        ('Olives', 'Olives'),
        ('Jalepenos', 'Jalepenos'),
        ('Cheese', 'Cheese'),
        ('Paneer', 'Paneer'),
        ('Pickle', 'Pickle'),
    )

    id = models.BigAutoField(primary_key=True)
    name = models.CharField( max_length = 50)
    size = models.CharField( max_length = 100, default=1, choices = SIZE_CHOICES)
    type = models.CharField( max_length = 500, default=1, choices = TYPE_CHOICES)
    topping = MultiSelectField(choices = TOPPINGS_CHOICES)


