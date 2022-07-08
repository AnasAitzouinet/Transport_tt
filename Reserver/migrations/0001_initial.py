# Generated by Django 4.0.5 on 2022-07-01 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='reserver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=220)),
                ('last_name', models.CharField(max_length=220)),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('adults', models.IntegerField()),
                ('kids', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('streetline_1', models.CharField(max_length=220)),
                ('streetline_2', models.CharField(max_length=220)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.IntegerField()),
                ('details', models.TextField(blank=b'I01\n')),
                ('excursion', models.CharField(max_length=200)),
                ('cars', models.CharField(max_length=200)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]