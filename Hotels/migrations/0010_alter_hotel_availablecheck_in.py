# Generated by Django 4.0.5 on 2022-07-03 11:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotels', '0009_alter_hotel_availablecheck_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='availablecheck_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 12, 30, 22, 980593)),
        ),
    ]
