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
    path('usaha/wia/<id>/', views.wia),
    path('usaha/wia10/<id>/', views.wia10),
    path('usaha/wia25/<id>/', views.wia25),
    path('usaha/wia50/<id>/', views.wia50),
    path('usaha/wia75/<id>/', views.wia75),
    path('usaha/wia100/<id>/', views.wia100),

    #lrk
    path('usaha/lrk/<id>/', views.lrk),
    path('usaha/notif/<id>/', views.indexnotif),

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
    path('<id>/edit_usaha',views.edit_usaha),
    path('usaha/<id>/edit_p_tunai/<id_p>',views.edit_p_tunai),
    path('usaha/<id>/edit_pend_lain/<id_p>',views.edit_pend_lain),
    path('usaha/<id>/edit_p_kredit/<id_p>',views.edit_p_kredit),
    path('usaha/<id>/edit_p_kredit_terima/<id_p>',views.edit_p_kredit_terima), #terima pembayaran
    path('usaha/<id>/edit_p_kredit_terima1/<id_p>',views.edit_p_kredit_terima1), #terima pembayaran1
    path('usaha/<id>/edit_pend_lain_terima/<id_p>',views.edit_pend_lain_terima), #terima pembayaran2
    path('usaha/<id>/edit_p_lain/<id_p>',views.edit_p_lain),
    path('usaha/<id>/edit_utang/<id_p>',views.edit_utang),
    path('usaha/<id>/edit_pend_lain/<id_p>',views.edit_pend_lain),
    path('usaha/<id>/edit_pem_tunai/<id_p>',views.edit_pem_tunai),
    path('usaha/<id>/edit_pem_kredit/<id_p>',views.edit_pem_kredit),
    # path('usaha/<id>/edit_pem_lain/<id_p>',views.edit_pem_lain),
    # path('usaha/<id>/edit_pembayaran_biaya/<id_p>',views.edit_pembayaran_biaya),
    # path('usaha/<id>/edit_pembayaran_lain/<id_p>',views.edit_pembayaran_lain),
    path('usaha/<id>/edit_barang/<id_p>',views.edit_barang),
    path('usaha/<id>/edit_butang/<id_p>',views.edit_butang),
    path('usaha/<id>/edit_butang1/<id_p>',views.edit_butang1),
    path('usaha/<id>/edit_butang2/<id_p>',views.edit_butang2),
    path('usaha/<id>/edit_butang3/<id_p>',views.edit_butang3),
    path('usaha/<id>/edit_saldoawal/<id_p>',views.edit_saldoawal),


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


    #bayar
    path('usaha/penjualan1bayar/<id>/', views.penjualan1bayar),

]
