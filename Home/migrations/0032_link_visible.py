# Generated by Django 4.2.3 on 2023-07-31 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0031_multipleimage_sequence'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='visible',
            field=models.BooleanField(default=True, verbose_name='Видимость'),
        ),
    ]
