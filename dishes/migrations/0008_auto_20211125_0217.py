# Generated by Django 3.2.9 on 2021-11-24 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0007_remove_categorydishes_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorydishes',
            options={'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='categorydishes',
            name='type_dishes',
            field=models.CharField(max_length=80),
        ),
    ]