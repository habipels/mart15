from django.shortcuts import render, HttpResponse
# Create your views here.

from kategori.models import *
def index(request):
    kategorlerim = kategoriler.objects.all()
    urunlerim = urunler.objects.all()
    bedenler = beden.objects.all()
    liste = []
    if favoriler.objects.filter(user_bilgisi = request.user):
        fav = favoriler.objects.filter(user_bilgisi = request.user)
        for i in fav:
            liste.append(i.urun_id)
    print(liste)
    sozluk = {"kategori":kategorlerim,"urunler":urunlerim,"bedenler":bedenler,"fav":liste}
    return render(request, "index.html",sozluk)

def kategori_index(request,id):
    kategorlerim = kategoriler.objects.all()
    urunlerim = urunler.objects.filter(urun_kategori_id = id)
    bedenler = beden.objects.all()
    sozluk = {"kategori":kategorlerim,"urunler":urunlerim,"id":id,"bedenler":bedenler}
    return render(request, "index.html",sozluk,)

def urun_tek(request,id):
    urunlerim = urunler.objects.filter(id = id)
    resim = resimler.objects.filter(urun_id = id)
    sozluk = {"urunler":urunlerim,"resim":resim}
    return render(request, "product_page.html",sozluk)