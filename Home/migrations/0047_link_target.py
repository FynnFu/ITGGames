# Generated by Django 4.2.3 on 2023-08-06 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0046_link_dynamic_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='target',
            field=models.BooleanField(default=False, verbose_name='Открывать в новой вкладке'),
        ),
    ]
