# Generated by Django 4.2.3 on 2023-07-31 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0030_multipleimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='multipleimage',
            name='sequence',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
