# Generated by Django 4.2.3 on 2023-07-21 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_socialmedia_alter_dropdownlink_href_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='video',
            field=models.CharField(default='', max_length=2000),
        ),
    ]