# Generated by Django 4.2.3 on 2023-07-19 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_remove_link_route_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='href',
            field=models.TextField(default=''),
        ),
    ]
