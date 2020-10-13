"""kelompok URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.halamandepan),
    path('penjualan_tunai/', views.penjualan_tunai),
    path('utang/', views.utang),
    path('piutang/', views.piutang),
    path('pembelian_tunai/', views.pembelian_tunai),
    path('pembayaran_utang/', views.pembayaran_utang),
    path('barang/', views.barang),
    path('lr/', views.lr),
    path('admin/', admin.site.urls),


    #crud
    path('penjualan1/', views.penjualan1v),
    path('utangv/', views.utangv),
    path('pend_lainv/', views.pend_lainv),
    path('pem_tunaiv/', views.pem_tunaiv),
    path('pem_kreditv/', views.pem_kreditv),
    path('pem_lainv/', views.pem_lainv),
    path('barangv/', views.barangv),

    #edit
    path('<id>/edit_p_tunai/',views.edit_p_tunai),
    path('<id>/edit_p_kredit/',views.edit_p_kredit),
    path('<id>/edit_p_kredit_terima/',views.edit_p_kredit_terima), #terima pembayaran
    path('<id>/edit_p_kredit_terima1/',views.edit_p_kredit_terima1), #terima pembayaran1
    path('<id>/edit_pend_lain_terima/',views.edit_pend_lain_terima), #terima pembayaran2

    path('<id>/edit_p_lain/',views.edit_p_lain),
    path('<id>/edit_utang/',views.edit_utang),
    path('<id>/edit_pend_lain/',views.edit_pend_lain),
    path('<id>/edit_pem_tunai/',views.edit_pem_tunai),
    path('<id>/edit_pem_kredit/',views.edit_pem_kredit),
    path('<id>/edit_pem_lain/',views.edit_pem_lain),
    path('<id>/edit_pembayaran_biaya/',views.edit_pembayaran_biaya),
    path('<id>/edit_pembayaran_lain/',views.edit_pembayaran_lain),
    path('<id>/edit_barang/',views.edit_barang),
    path('<id>/edit_butang/',views.edit_butang),
    path('<id>/edit_butang1/',views.edit_butang1),
    path('<id>/edit_butang2/',views.edit_butang2),
    path('<id>/edit_butang3/',views.edit_butang3),
    path('<id>/edit_saldoawal/',views.edit_saldoawal),


    #Hapus
    path('<id>/hapus1/',views.hapus1),
    path('<id>/hapus2/',views.hapus2),
    path('<id>/hapus3/',views.hapus3),
    path('<id>/hapus4/',views.hapus4),
    path('<id>/hapus5/',views.hapus5),
    path('<id>/hapus6/',views.hapus6),
    path('<id>/hapus7/',views.hapus7),
    path('<id>/hapus8/',views.hapus8),
    path('<id>/hapus9/',views.hapus9),
    path('<id>/hapus10/',views.hapus10),
    path('<id>/hapus11/',views.hapus11),
    # path('<id>/edit_pembayaran_lain/',views.edit_pembayaran_lain),
    # path('<id>/edit_barang/',views.edit_barang),
]
