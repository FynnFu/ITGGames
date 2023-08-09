# Generated by Django 4.2.3 on 2023-08-07 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0053_rename_image_news_main_image_remove_news_images'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MultipleImage',
            new_name='MultipleImageGame',
        ),
        migrations.CreateModel(
            name='MultipleImageNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='')),
                ('sequence', models.PositiveIntegerField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.game')),
            ],
        ),
    ]