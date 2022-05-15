from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class kategoriler(models.Model):
    kategori_isim = models.CharField(max_length=100)
    def __str__(self):
        return self.kategori_isim

class beden(models.Model):
    beden_isim = models.CharField(max_length=10)
    def __str__(self):
        return self.beden_isim
class urunler(models.Model):
    urun_kategori = models.ForeignKey(kategoriler, on_delete=models.SET_NULL,null=True)
    urun_beden = models.ForeignKey(beden, on_delete=models.CASCADE,null=True)
    urun_resim = models.FileField(upload_to='urunresim/',blank = True,null = True,verbose_name="Ürün Resim")
    urun_isimi =models.CharField(max_length=100)
    urun_stog =models.IntegerField()
    urun_fiyat = models.IntegerField()
    urun_aciklama = RichTextField(null=True)
    def __str__(self):
        return self.urun_isimi

class resimler(models.Model):
    urun = models.ForeignKey(urunler, on_delete=models.SET_NULL,null=True)
    urun_resim = models.FileField(upload_to='urunresim/',blank = True,null = True,verbose_name="Ürün Resim")

from django.contrib.auth.models import User
class favoriler(models.Model):
    user_bilgisi = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    urun = models.ForeignKey(urunler, on_delete=models.CASCADE,null=True)


