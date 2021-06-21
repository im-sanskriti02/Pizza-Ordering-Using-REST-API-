from .models import Pizza 
from rest_framework import serializers

class PizzaSerializer(serializers.ModelSerializer):

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

    topping = serializers.MultipleChoiceField(choices=TOPPINGS_CHOICES)

    class Meta:
    
        model = Pizza
        fields = ('id', 'name', 'type', 'size', 'topping')