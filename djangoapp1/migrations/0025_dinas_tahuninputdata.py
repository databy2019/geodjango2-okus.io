# Generated by Django 2.2 on 2021-03-23 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp1', '0024_auto_20210323_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='dinas',
            name='tahunInputData',
            field=models.IntegerField(default=2021),
        ),
    ]