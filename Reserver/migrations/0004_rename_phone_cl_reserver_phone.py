# Generated by Django 4.0.5 on 2022-07-03 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reserver', '0003_reserver_phone_cl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserver',
            old_name='phone_cl',
            new_name='phone',
        ),
    ]
