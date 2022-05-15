from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('register/',views.kayit,name = "register"),
    path('login/',views.giris,name = "login"),
    path('logout/',views.cikis,name = "logout"),
]
