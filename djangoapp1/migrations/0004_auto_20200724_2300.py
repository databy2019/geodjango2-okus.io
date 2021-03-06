# Generated by Django 3.0.8 on 2020-07-24 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp1', '0003_auto_20200724_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kegiatansarpras',
            name='keterangan',
            field=models.TextField(max_length=300, null=True, verbose_name='Keterangan'),
        ),
        migrations.AlterField(
            model_name='kegiatansarpras',
            name='kodeKegiatan',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Kode Kegiatan'),
        ),
        migrations.AlterField(
            model_name='kegiatansarpras',
            name='namaKegiatan',
            field=models.CharField(max_length=200, verbose_name='Nama Kegiatan'),
        ),
        migrations.AlterField(
            model_name='programsarpras',
            name='keterangan',
            field=models.TextField(max_length=300, verbose_name='Keterangan'),
        ),
        migrations.AlterField(
            model_name='programsarpras',
            name='kodeProgram',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='Kode Program'),
        ),
        migrations.AlterField(
            model_name='programsarpras',
            name='namaProgram',
            field=models.CharField(max_length=200, verbose_name='Nama Program'),
        ),
    ]
