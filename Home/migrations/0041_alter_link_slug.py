# Generated by Django 4.2.3 on 2023-08-06 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0040_alter_link_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='slug',
            field=models.SlugField(blank=True, default='', unique=True, verbose_name='URL'),
        ),
    ]
