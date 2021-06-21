# Generated by Django 2.2 on 2021-03-23 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp1', '0022_dinas_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dinas',
            old_name='tahun',
            new_name='tahunInput',
        ),
        migrations.AddField(
            model_name='dinas',
            name='anggaran2017',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='dinas',
            name='anggaran2018',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='dinas',
            name='anggaran2019',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='dinas',
            name='anggaran2020',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='dinas',
            name='anggaran2021',
            field=models.FloatField(default=0.0),
        ),
    ]