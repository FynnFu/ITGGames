# Generated by Django 4.2.3 on 2023-07-21 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0018_alter_game_release_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='video',
            new_name='video_src',
        ),
    ]
