# Generated by Django 3.2.4 on 2021-06-21 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20210621_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toppings',
            name='t2',
        ),
        migrations.AddField(
            model_name='toppings',
            name='toppings',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
