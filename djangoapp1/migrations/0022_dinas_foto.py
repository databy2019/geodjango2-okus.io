# Generated by Django 2.2 on 2021-03-23 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp1', '0021_auto_20210323_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='dinas',
            name='foto',
            field=models.ImageField(null=True, upload_to='static/uploads/%Y/%m/%d'),
        ),
    ]