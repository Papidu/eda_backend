# Generated by Django 3.2.9 on 2021-11-24 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0006_auto_20211125_0212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorydishes',
            name='name',
        ),
    ]
