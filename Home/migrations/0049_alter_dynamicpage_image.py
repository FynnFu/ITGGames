# Generated by Django 4.2.3 on 2023-08-06 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0048_dropdownlink_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dynamicpage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/dynamic_page/'),
        ),
    ]
