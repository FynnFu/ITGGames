# Generated by Django 4.2.3 on 2023-08-02 08:38

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0036_rename_systemrequirement_systemrequirements'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='systemrequirements',
            options={'verbose_name': 'SystemRequirements', 'verbose_name_plural': 'SystemRequirements'},
        ),
        migrations.AddField(
            model_name='systemrequirements',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='systemrequirements',
            name='requirements',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AlterField(
            model_name='systemrequirements',
            name='requirements_recommended',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]
