# Generated by Django 4.1.7 on 2023-03-01 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_alter_album_artist_alter_album_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
