# Generated by Django 4.0.5 on 2022-07-03 10:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Listings', '0004_admin_add_listings_availablecheck_out_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_add',
            name='availablecheck_inadd',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 11, 3, 38, 851466)),
        ),
        migrations.AlterField(
            model_name='admin_add',
            name='availablecheck_outadd',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 11, 3, 38, 851466)),
        ),
        migrations.AlterField(
            model_name='listings',
            name='availablecheck_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 11, 3, 38, 849466)),
        ),
        migrations.AlterField(
            model_name='listings',
            name='availablecheck_out',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 11, 3, 38, 849466)),
        ),
    ]
