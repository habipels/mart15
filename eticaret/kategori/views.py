from django.shortcuts import render , redirect
from .models import favoriler
# Create your views here.

def fav_ekle(request,id):
    favoriler.objects.create(user_bilgisi = request.user,urun_id = id)
    return redirect("index")

def fav_sil(request,id):
    favoriler.objects.filter(urun_id = id).delete()
    return redirect("index")