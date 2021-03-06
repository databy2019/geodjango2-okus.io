# Generated by Django 3.0.8 on 2020-08-05 10:02

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp1', '0013_jalankabupaten'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jalankabupaten',
            options={'ordering': ('kodeJalanK',), 'verbose_name_plural': '5. Jalan Kabupaten'},
        ),
        migrations.AlterModelOptions(
            name='jalanpropinsi',
            options={'ordering': ('kodeJalanP',), 'verbose_name_plural': '4. Jalan Propinsi'},
        ),
        migrations.AlterModelOptions(
            name='sarpras',
            options={'ordering': ('kodeSarpras',), 'verbose_name_plural': '6. Kegiatan Sarana dan Prasarana'},
        ),
        migrations.CreateModel(
            name='InfrastrukturJalan',
            fields=[
                ('kodeInfrastrukturJ', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('namaInfrastrukturJ', models.CharField(max_length=150)),
                ('tahun', models.IntegerField()),
                ('foto', models.ImageField(null=True, upload_to='static/uploads/%Y/%m/%d')),
                ('lokasi', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('keterangan', models.TextField(max_length=300)),
                ('kodeKegiatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoapp1.KegiatanSarpras')),
            ],
            options={
                'verbose_name_plural': '7. Kegiatan Infrastruktur Jalan',
                'ordering': ('kodeInfrastrukturJ',),
            },
        ),
    ]
