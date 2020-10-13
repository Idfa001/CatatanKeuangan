from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class barangm(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='barang')
    barang = models.CharField(max_length=200)
    harga_beli = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    harga_jual = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    
    def __str__(self):
        return self.barang
 
class saldoawalm(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='saldoawal')
    saldo_awal = models.DecimalField(default=0, max_digits=10, decimal_places=0)

class SaldoAwal(models.Model):
    saldo_awal = models.IntegerField(default=0)

class penjualan1m(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='penjualan')
    tanggal = models.DateField(auto_now_add=True)
    barang = models.ForeignKey(barangm, on_delete = models.DO_NOTHING)
    kuantitas = models.IntegerField(default=0)
    saldo_awal = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    kas_masuk = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    terima = models.IntegerField(default=0)

     
    def tanggal1(self):
        return self.tanggal.strftime("%d-%m-%Y")

    def total(self):
        return self.barang.harga_jual * self.kuantitas

    def piutang(self):
        return self.total() - self.kas_masuk

    def kas_masuk1(self):
        return self.kas_masuk
    
    def piutang1(self):
        return self.piutang()

    def saldo(self):
        return self.piutang() - self.terima

class utangm(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='utang')
    tanggal = models.DateField(auto_now_add=True)
    catatan = models.CharField(max_length=200)
    jumlah = models.DecimalField(max_digits=10, decimal_places=0)
    jatuh_tempo = models.DateField(default=datetime.now)
    dibayar = models.DecimalField(default=0, max_digits=10, decimal_places=0)

    def tanggal1(self):
        return self.tanggal.strftime("%d-%m-%Y")

    def tanggal2(self):
        return self.jatuh_tempo.strftime("%d-%m-%Y")

    def jum_utang(self):
        return self.jumlah

    def saldo(self):
        return self.jumlah - self.dibayar

    def jumlah3(self):
        return self.saldo()

    def duda(self):
        return self.jatuh_tempo - datetime.now().date()
    
    def jatempo(self):
        return self.duda().days

class pend_lainm(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='pendlain')
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    pendapatan = models.DecimalField(max_digits=10, decimal_places=0)
    kas_masuk = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    terima  = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    def tanggal1(self):
        return self.tanggal.strftime("%d/%m/%Y")

    def jum_pend(self): 
        return self.kas_masuk

    def jum_pend1(self):
        return self.pendapatan

    
    def piutang1(self):
        return self.pendapatan - self.kas_masuk
    
    def jum_pend3(self):
        return self.piutang1()
    
    def saldo(self):
        return self.piutang1() - self.terima


class pem_tunaim(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='pemtunai')
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    pembelian = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    kas_keluar = models.DecimalField(max_digits=10, decimal_places=0)
    dibayar = models.DecimalField(default=0, max_digits=10, decimal_places=0)


    def tanggal1(self):
        return self.tanggal.strftime("%d/%m/%Y")

    def jum_pem(self):
        return self.jumlah
    
    def kas_keluar1(self):
        return self.kas_keluar
    
    def pembelian1(self):
        return self.pembelian
    
    def utang(self):
        return self.pembelian - self.kas_keluar

    def utang1(self):
        return self.utang()
    
    def saldo(self):
        return self.utang() - self.dibayar
    
    def saldo1(self):
        return self.saldo()

class pem_kreditm(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='pemkredit')
    tanggal = models.DateField(auto_now_add=True)
    barang = models.ForeignKey(barangm, on_delete = models.DO_NOTHING)
    kuantitas = models.IntegerField(default=0)
    kas_keluar = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    dibayar1 = models.DecimalField(default=0, max_digits=10, decimal_places=0)

    def tanggal1(self):
        return self.tanggal.strftime("%d/%m/%Y")

    def jum_pem(self):
        return self.jumlah

    def saldo(self):
        return self.jumlah - self.dibayar1

    def total(self):
        return self.barang.harga_beli * self.kuantitas
    
    def utang(self):
        return self.total() - self.kas_keluar

    def kas_keluar2(self):
        return self.kas_keluar

    def pembelian2(self):
        return self.total()

    def utang2 (self):
        return self.utang()

    def saldo1 (self):
        return self.utang() - self.dibayar1

    def saldo2 (self):
        return self.saldo1()
        
class pem_lainm(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='pemlain')
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    dibayar = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    utang = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    catatan = models.CharField(max_length=200)
    dibayar2 = models.DecimalField(default=0, max_digits=10, decimal_places=0)

    def tanggal1(self):
        return self.tanggal.strftime("%d/%m/%Y")

    def jum_pem(self):
        return self.dibayar

    def jum_pem1(self):
        return self.utang

    def saldo(self):
        return self.utang - self.dibayar2


class pembayaran_biayam(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='pembiaya')
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    dibayar = models.DecimalField(max_digits=10, decimal_places=0)
    catatan = models.CharField(max_length=200)

    def tanggal1(self):
        return self.tanggal.strftime("%d/%m/%Y")

    def jum_pem(self):
        return self.dibayar

class pembayaran_lainm(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='pembayaranlain')
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    dibayar = models.DecimalField(max_digits=10, decimal_places=0)
    utang = models.DecimalField(max_digits=10, decimal_places=0)
    catatan = models.CharField(max_length=200)
    dibayar3 = models.DecimalField(default=0, max_digits=10, decimal_places=0)

    def tanggal1(self):
        return self.tanggal.strftime("%d/%m/%Y")

    def jum1(self):
        return self.dibayar

    def jum2(self):
        return self.utang

    def saldo(self):
        return self.utang - self.dibayar3


    

