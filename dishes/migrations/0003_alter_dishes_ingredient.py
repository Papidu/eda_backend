# Generated by Django 3.2.9 on 2021-11-24 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0002_auto_20211124_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishes',
            name='ingredient',
            field=models.ManyToManyField(blank=True, to='dishes.Ingredients'),
        ),
    ]
