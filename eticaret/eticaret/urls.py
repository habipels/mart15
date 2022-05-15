"""eticaret URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from alltemplate.views import *
from django.conf import settings
from django.conf.urls.static import static
from kategori.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name="index"),
    path("urun/<int:id>",urun_tek,name="urun"),
    path("kategori/<int:id>",kategori_index,name="kategori_goster"),
    path("user/",include("user_o.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("fav/<int:id>",fav_ekle,name="favori"),
    path("favs/<int:id>",fav_sil,name="fav_sil"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
