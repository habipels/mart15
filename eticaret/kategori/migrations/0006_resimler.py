# Generated by Django 3.2.9 on 2022-04-28 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kategori', '0005_urunler_urun_aciklama'),
    ]

    operations = [
        migrations.CreateModel(
            name='resimler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urun_resim', models.FileField(blank=True, null=True, upload_to='urunresim/', verbose_name='Ürün Resim')),
                ('urun', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kategori.urunler')),
            ],
        ),
    ]
