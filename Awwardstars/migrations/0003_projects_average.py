# Generated by Django 3.1.2 on 2020-10-29 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Awwardstars', '0002_auto_20201028_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='average',
            field=models.IntegerField(default=0),
        ),
    ]
