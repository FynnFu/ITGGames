# Generated by Django 4.2.3 on 2023-07-19 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_game_alter_dropdownlink_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='dropdownlink',
            name='href',
            field=models.TextField(default=''),
        ),
    ]
