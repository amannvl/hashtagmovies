# Generated by Django 3.0.5 on 2020-05-03 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashtagmovies', '0003_delete_movielist'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='movie_id',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
