# Generated by Django 5.0.4 on 2024-04-05 22:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 22, 36, 24, 775560, tzinfo=datetime.timezone.utc)),
        ),
    ]
