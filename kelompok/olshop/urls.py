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
    path('', views.usaha),
    path('haldepan/', views.halamandepan),
    path('usaha/penjualan_tunai/<id>/', views.penjualan_tunai),
    path('usaha/utang/<id>/', views.utang),
    path('usaha/piutang/<id>/', views.piutang),
    path('usaha/pembelian_tunai/<id>/', views.pembelian_tunai),
    path('usaha/pembayaran_utang/<id>/', views.pembayaran_utang),
    path('usaha/barang/<id>/', views.barang),
    path('usaha/', views.usaha),
    path('usaha/lr/<id>/', views.lr),
    path('admin/', admin.site.urls),
    path('usaha/haldepan/<id>/', views.halamandepan),

    #crud
    path('usaha/penjualan1/<id>/', views.penjualan1v),
    path('usaha/utangv/<id>/', views.utangv),
    path('usaha/pend_lainv/<id>/', views.pend_lainv),
    path('usaha/pem_tunaiv/<id>/', views.pem_tunaiv),
    path('usaha/pem_kreditv/<id>/', views.pem_kreditv),
    path('usaha/pem_lainv/<id>/', views.pem_lainv),
    path('usaha/barangv/<id>/', views.barangv),
    path('usahav/', views.usahav),



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
    path('usaha/<id>/hapus1/<id_p>',views.hapus1),
    path('usaha/<id>/hapus2/<id_p>',views.hapus2),
    path('usaha/<id>/hapus3/<id_p>',views.hapus3),
    path('usaha/<id>/hapus4/<id_p>',views.hapus4),
    path('usaha/<id>/hapus5/<id_p>',views.hapus5),
    path('usaha/<id>/hapus6/<id_p>',views.hapus6),
    path('usaha/<id>/hapus7/<id_p>',views.hapus7),
    path('usaha/<id>/hapus8/<id_p>',views.hapus8),
    path('usaha/<id>/hapus9/<id_p>',views.hapus9),
    path('usaha/<id>/hapus10/<id_p>',views.hapus10),
    path('usaha/<id>/hapus11/<id_p>',views.hapus11),
    path('<id>/hapus12/',views.hapus12),
    # path('<id>/edit_pembayaran_lain/',views.edit_pembayaran_lain),
    # path('<id>/edit_barang/',views.edit_barang),
]
