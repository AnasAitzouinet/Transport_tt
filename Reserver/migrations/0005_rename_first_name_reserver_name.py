# Generated by Django 4.0.5 on 2022-07-03 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reserver', '0004_rename_phone_cl_reserver_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserver',
            old_name='first_name',
            new_name='name',
        ),
    ]