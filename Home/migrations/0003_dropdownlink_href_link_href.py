# Generated by Django 4.2.3 on 2023-07-17 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_rename_links_dropdownlink_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='dropdownlink',
            name='href',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='link',
            name='href',
            field=models.TextField(default=''),
        ),
    ]
