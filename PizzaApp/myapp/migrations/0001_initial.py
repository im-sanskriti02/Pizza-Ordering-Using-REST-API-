# Generated by Django 3.2.4 on 2021-06-20 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('size', models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], default=1, max_length=100)),
                ('type', models.CharField(choices=[('Regular', 'Regular'), ('Square', 'Square')], default=1, max_length=500)),
                ('topping', models.CharField(choices=[('Onion', 'Onion'), ('Tomato', 'Tomato'), ('Capsicum', 'Capsicum'), ('Corn', 'Corn'), ('Olives', 'Olives'), ('Jalepenos', 'Jalepenos'), ('Cheese', 'Cheese'), ('Paneer', 'Paneer'), ('Pickle', 'Pickle')], max_length=200)),
                ('description', models.CharField(max_length=5000, null=True)),
            ],
        ),
    ]
