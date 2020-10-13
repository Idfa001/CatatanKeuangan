from django.shortcuts import render, redirect
from django.db.models import Sum
from bootstrap_datepicker_plus import DatePickerInput
from . import models, forms
from account.forms import CreateUserForm


def halamandepan(req):
    if not req.user.is_authenticated:
        return redirect ('/account')
 
    pen = models.penjualan1m.objects.all()
    pen2 = models.pend_lainm.objects.all()

    pen = models.penjualan1m.objects.filter(owner=req.user)
    pen2 = models.pend_lainm.objects.filter(owner=req.user)


    kas_masuk1 = 0
    for q in pen:
      kas_masuk1 += q.kas_masuk1()

    kas_masuk2 = 0
    for q in pen2:
      kas_masuk2 += q.jum_pend()

    penjualan1 = models.penjualan1m.objects.all()
    penjualan2 = models.pend_lainm.objects.all()

    penjualan1 = models.penjualan1m.objects.filter(owner=req.user)
    penjualan2 = models.pend_lainm.objects.filter(owner=req.user)

    total_terima1 = 0   

    for p in penjualan1:
      total_terima1 += p.terima

    total_terima2 = 0   

    for p in penjualan2:
      total_terima2 += p.terima

    kas_masuk3 = total_terima1 + total_terima2

    utang = models.utangm.objects.all()
    utang = models.utangm.objects.filter(owner=req.user)

    kas_masuk4 = 0
    for i in utang:
      kas_masuk4 += i.jum_utang()

    pem = models.pem_tunaim.objects.all()
    pem1 = models.pem_kreditm.objects.all()

    pem = models.pem_tunaim.objects.filter(owner=req.user)
    pem1 = models.pem_kreditm.objects.filter(owner=req.user)

    kas_keluar1 = 0
    for i in pem:
      kas_keluar1 += i.kas_keluar1()

    kas_keluar2 = 0
    for i in pem1:
      kas_keluar2 += i.kas_keluar2()

    utang = models.utangm.objects.all()
    pem = models.pem_kreditm.objects.all()
    pem1 = models.pem_tunaim.objects.all()

    utang = models.utangm.objects.filter(owner=req.user)
    pem = models.pem_kreditm.objects.filter(owner=req.user)
    pem1 = models.pem_tunaim.objects.filter(owner=req.user)


    bayar11 = 0

    for p in pem:
        bayar11 += p.dibayar1
    
    bayar22 = 0

    for q in utang:
        bayar22 += q.dibayar
    
    bayar33 = 0

    for r in pem1:
        bayar33 += r.dibayar

    kas_keluar3 = bayar11 + bayar22 + bayar33

    jumlah1 = kas_masuk1 + kas_masuk2 + kas_masuk3 + kas_masuk4
    jumlah2 = kas_keluar1 + kas_keluar2 + kas_keluar3

    total = jumlah1 - jumlah2
    
    pend = models.pend_lainm.objects.all()
    penjualan1 = models.penjualan1m.objects.all()
    penjualan2 = models.pend_lainm.objects.all()

    pend = models.pend_lainm.objects.filter(owner=req.user)
    penjualan1 = models.penjualan1m.objects.filter(owner=req.user)
    penjualan2 = models.pend_lainm.objects.filter(owner=req.user)

    total_saldo1 = 0  

    for p in penjualan1:
      total_saldo1 += p.saldo()

    total_saldo2 = 0

    for p in pend:
      total_saldo2 += p.saldo()

    saldo_total1 = total_saldo1 + total_saldo2

    utang = models.utangm.objects.all()
    pem = models.pem_kreditm.objects.all()
    pem1 = models.pem_tunaim.objects.all()

    utang = models.utangm.objects.filter(owner=req.user)
    pem = models.pem_kreditm.objects.filter(owner=req.user)
    pem1 = models.pem_tunaim.objects.filter(owner=req.user)

    saldo11 = 0

    for p in pem:
        saldo11 += p.saldo2()
    
    saldo22 = 0

    for q in utang:
        saldo22 += q.jumlah3()
    
    saldo33 = 0

    for r in pem1:
        saldo33 += r.saldo1()

    jumlah10 = saldo11 + saldo22 + saldo33


    return render(req, 'hal1/index1.html', {
    'kas_masuk1': kas_masuk1,
    'kas_masuk2': kas_masuk2,
    'kas_masuk3': kas_masuk3,
    'kas_masuk4': kas_masuk4,
    'kas_keluar1': kas_keluar1,
    'kas_keluar2': kas_keluar2,
    'kas_keluar3': kas_keluar3,
    'jumlah1': jumlah1,
    'jumlah10': jumlah10,
    'jumlah2': jumlah2,
    'total': total,
    'saldo_total1': saldo_total1,

    })

def penjualan_tunai(req):  
      
    if req.GET and req.GET["dari"] and req.GET["sampai"]: 
        penjualan1 = models.penjualan1m.objects.filter(tanggal__range=[req.GET["dari"], req.GET["sampai"]])
        penjualan2 = models.pend_lainm.objects.filter(tanggal__range=[req.GET["dari"], req.GET["sampai"]])
 
    else:
        penjualan1 = models.penjualan1m.objects.all()
        penjualan2 = models.pend_lainm.objects.all()
    
    penjualan1 = penjualan1.filter(owner=req.user)
    penjualan2 = penjualan2.filter(owner=req.user)
    total = 0
    for p in penjualan1:
      total += p.total()
      
    kas_masuk1 = 0
    for q in penjualan1:
      kas_masuk1 += q.kas_masuk1()
    
    piutang1 = 0
    for r in penjualan1:
      piutang1 += r.piutang1()
    

    jum_pend = 0
    for t in penjualan2:
      jum_pend += t.jum_pend()

    jum_pend3 = 0
    for u in penjualan2:
      jum_pend3 += u.jum_pend3()

    jum_pend1 = 0
    for s in penjualan2:
      jum_pend1 += s.jum_pend1()
    return render(req, 'penjualan/index3.html', {
        'data': penjualan1,
        'data1': penjualan2,
        'jum_pend1':jum_pend1,
        'jum_pend': jum_pend,
        'jum_pend3':jum_pend3,
        'kas_masuk1': kas_masuk1,
        'piutang1': piutang1,
        'total': total,
    })

def piutang(req):
    pend = models.pend_lainm.objects.all()
    penjualan1 = models.penjualan1m.objects.all()
    penjualan2 = models.pend_lainm.objects.all()

    pend = models.pend_lainm.objects.filter(owner=req.user)
    penjualan1 = models.penjualan1m.objects.filter(owner=req.user)
    penjualan2 = models.pend_lainm.objects.filter(owner=req.user)

    total_saldo1 = 0
    total_terima1 = 0   

    for p in penjualan1:
      total_saldo1 += p.saldo()
      total_terima1 += p.terima

    total_saldo2 = 0
    total_terima2 = 0   

    for p in pend:
      total_saldo2 += p.saldo()
      total_terima2 += p.terima

    saldo_total1 = total_saldo1 + total_saldo2
    saldo_total2 = total_terima1 + total_terima2
    return render(req, 'uangmasuk/index6.html', {
        'data2': pend,
        'data' :penjualan1,
        'data1' :penjualan2,
        'saldo_total1': saldo_total1,
        'saldo_total2': saldo_total2,
        
    })

def utang(req):
    task = models.utangm.objects.filter(owner=req.user)
    form_input = forms.utangf()
    if req.POST:
        form_input = forms.utangf(req.POST)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
        return redirect('/utang')

    utang = models.utangm.objects.all()
    utang = models.utangm.objects.filter(owner=req.user)

    jum_utang = 0
    for i in utang:
      jum_utang += i.jum_utang()

    return render(req, 'uangmasuk/index7.html', {
        'data': utang,
        'data': task,
        'jum_utang': jum_utang,
        'form': form_input,        
    })

def pembelian_tunai(req):
    task = models.pem_tunaim.objects.filter(owner=req.user)
    form_input = forms.pem_tunaif()
    if req.POST:
        form_input = forms.pem_tunaif(req.POST)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
        return redirect('/pembelian_tunai')
    pem = models.pem_tunaim.objects.all()
    pem1 = models.pem_kreditm.objects.all()

    pem = pem.filter(owner=req.user)
    pem1 = pem1.filter(owner=req.user)

    kas_keluar1 = 0
    pembelian1 = 0
    utang1 = 0
    for i in pem:
      kas_keluar1 += i.kas_keluar1()
      pembelian1 += i.pembelian1()
      utang1 += i.utang1()


    kas_keluar2 = 0
    pembelian2 = 0
    utang2 = 0
    for i in pem1:
      kas_keluar2 += i.kas_keluar2()
      pembelian2 += i.pembelian2()
      utang2 += i.utang2()

    return render(req, 'pembelian/index10.html', {
        'data': pem,
        'data': task,
        'data1': pem1,
        'kas_keluar1': kas_keluar1,
        'kas_keluar2': kas_keluar2,
        'pembelian1' : pembelian1,
        'pembelian2' : pembelian2,
        'utang1': utang1,
        'utang2': utang2,
        'form': form_input,
    })




def pembayaran_utang(req):
    
    utang = models.utangm.objects.all()
    pem = models.pem_kreditm.objects.all()
    pem1 = models.pem_tunaim.objects.all()

    utang = models.utangm.objects.filter(owner=req.user)
    pem = models.pem_kreditm.objects.filter(owner=req.user)
    pem1 = models.pem_tunaim.objects.filter(owner=req.user)

    saldo11 = 0
    bayar11 = 0

    for p in pem:
        saldo11 += p.saldo2()
        bayar11 += p.dibayar1

    
    saldo22 = 0
    bayar22 = 0

    for q in utang:
        saldo22 += q.jumlah3()
        bayar22 += q.dibayar
    
    saldo33 = 0
    bayar33 = 0

    for r in pem1:
        saldo33 += r.saldo1()
        bayar33 += r.dibayar

    jumlah1 = saldo11 + saldo22 + saldo33
    jumlah2 = bayar11 + bayar22 + bayar33


    return render(req, 'uangkeluar/index13.html', {
        'data': utang,
        'data1': pem,
        'data2': pem1,
        'jumlah1' : jumlah1,
        'jumlah2' : jumlah2,
    })



def barang(req):
    task = models.barangm.objects.filter(owner=req.user)
    form_input = forms.barangf()
    if req.POST:
        form_input = forms.barangf(req.POST)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
        return redirect('/barang')
    return render(req, 'keperluan/index18.html', {
        'data': task,
        'form': form_input,
    })

def lr(req):
    if  req.POST:
        saldo_awal = models.SaldoAwal.objects.first()

        if saldo_awal:
            models.SaldoAwal.objects.update(saldo_awal=req.POST['saldo_awal'])
        else:
            models.SaldoAwal.objects.create(saldo_awal=req.POST['saldo_awal'])

        return redirect('/lr')





    pen = models.penjualan1m.objects.all()
    pen2 = models.pend_lainm.objects.all()

    pen = models.penjualan1m.objects.filter(owner=req.user)
    pen2 = models.pend_lainm.objects.filter(owner=req.user)

    kas_masuk1 = 0
    for q in pen:
      kas_masuk1 += q.kas_masuk1()

    kas_masuk2 = 0
    for q in pen2:
      kas_masuk2 += q.jum_pend()

    penjualan1 = models.penjualan1m.objects.all()
    penjualan2 = models.pend_lainm.objects.all()

    penjualan1 = models.penjualan1m.objects.filter(owner=req.user)
    penjualan2 = models.pend_lainm.objects.filter(owner=req.user)

    total_terima1 = 0   

    for p in penjualan1:
      total_terima1 += p.terima

    total_terima2 = 0   

    for p in penjualan2:
      total_terima2 += p.terima

    kas_masuk3 = total_terima1 + total_terima2

    utang = models.utangm.objects.all()
    kas_masuk4 = 0
    for i in utang:
      kas_masuk4 += i.jum_utang()

    pem = models.pem_tunaim.objects.all()
    pem1 = models.pem_kreditm.objects.all()

    pem = models.pem_tunaim.objects.filter(owner=req.user)
    pem1 = models.pem_kreditm.objects.filter(owner=req.user)

    kas_keluar1 = 0
    for i in pem:
      kas_keluar1 += i.kas_keluar1()

    kas_keluar2 = 0
    for i in pem1:
      kas_keluar2 += i.kas_keluar2()

    utang = models.utangm.objects.all()
    pem = models.pem_kreditm.objects.all()
    pem1 = models.pem_tunaim.objects.all()

    utang = models.utangm.objects.filter(owner=req.user)
    pem = models.pem_kreditm.objects.filter(owner=req.user)
    pem1 = models.pem_tunaim.objects.filter(owner=req.user)

    bayar11 = 0

    for p in pem:
        bayar11 += p.dibayar1
    
    bayar22 = 0

    for q in utang:
        bayar22 += q.dibayar
    
    bayar33 = 0

    for r in pem1:
        bayar33 += r.dibayar

    kas_keluar3 = bayar11 + bayar22 + bayar33

    jumlah1 = kas_masuk1 + kas_masuk2 + kas_masuk3 + kas_masuk4
    jumlah2 = kas_keluar1 + kas_keluar2 + kas_keluar3

    total = jumlah1 - jumlah2

    saldo_awal = models.SaldoAwal.objects.first()

    saldo_awal1 = models.SaldoAwal.objects.all()

    saldo1 = 0
    for p in saldo_awal1:
        saldo1 += p.saldo_awal

    saldo = saldo1 + total
       
    return render(req, 'keperluan/index16.html', {
    'kas_masuk1': kas_masuk1,
    'kas_masuk2': kas_masuk2,
    'kas_masuk3': kas_masuk3,
    'kas_masuk4': kas_masuk4,
    'kas_keluar1': kas_keluar1,
    'kas_keluar2': kas_keluar2,
    'kas_keluar3': kas_keluar3,
    'jumlah1': jumlah1,
    'jumlah2': jumlah2,
    'total': total,
    'data': saldo_awal,
    'saldo': saldo,
    })






#crud

def penjualan1v(req):
    task = models.penjualan1m.objects.filter(owner=req.user)
    form_input = forms.penjualan1f(user=req.user)
    if req.POST:
        form_input = forms.penjualan1f(req.POST, user=req.user)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
            return redirect('/penjualan_tunai')
    return render(req, 'crud/penjualan1.html', {
        'form': form_input,
        'data': task,
    })



def utangv(req):
    task = models.barangm.objects.filter(owner=req.user)
    form_input = forms.utangf()
    if req.POST:
        form_input = forms.utangf(req.POST)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
        return redirect('/utang')
    return render(req, 'crud/utang.html', {
        'form': form_input,
        'data': task,
    })

def pend_lainv(req):
    task = models.pend_lainm.objects.filter(owner=req.user)
    form_input = forms.pend_lainf()
    if req.POST:
        form_input = forms.pend_lainf(req.POST)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
        return redirect('/penjualan_tunai')
    return render(req, 'crud/pend_lain.html', {
        'form': form_input,
        'data': task,
    })

def pem_tunaiv(req):
    task = models.barangm.objects.filter(owner=req.user)
    form_input = forms.pem_tunaif()
    if req.POST:
        form_input = forms.pem_tunaif(req.POST)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
        return redirect('/pembelian_tunai')
    return render(req, 'crud/pem_tunai.html', {
        'form': form_input,
        'data': task,
    })

def pem_kreditv(req):
    task = models.barangm.objects.filter(owner=req.user)
    form_input = forms.pem_kreditf(user=req.user)
    if req.POST:
        form_input = forms.pem_kreditf(req.POST, user=req.user)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
        return redirect('/pembelian_tunai')
    return render(req, 'crud/pem_kredit.html', {
        'form': form_input,
        'data': task,
    })

def pem_lainv(req):
    task = models.barangm.objects.filter(owner=req.user)
    form_input = forms.pem_lainf(owner=req.user)
    if req.POST:
        form_input = forms.pem_lainf(req.POST)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
        return redirect('/pembelian_lain')
    return render(req, 'crud/pem_lain.html', {
        'form': form_input,
        'data': task,
    })


def barangv(req):
    form_input = forms.barangf()
    if req.POST:
        form_input = forms.barangf(req.POST)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
        return redirect('/barang')
    return render(req, 'crud/barang.html', {
        'form': form_input,
    })






#edit
def edit_p_tunai(req, id):
    if req.POST:
        models.penjualan1m.objects.filter(pk=id).update(kuantitas=req.POST['kuantitas'], kas_masuk=req.POST['kas_masuk'])
        return redirect('/penjualan_tunai')

    penjualan = models.penjualan1m.objects.filter(pk=id).first()
    return render(req, 'penjualan/edit_p_tunai.html', {
        'data': penjualan,
    })

def edit_p_kredit(req, id):
    if req.POST:
        models.penjualan2m.objects.filter(pk=id).update(kuantitas=req.POST['kuantitas'], catatan=req.POST['catatan'], jatuh_tempo=req.POST['jatuh_tempo'])
        return redirect('/penjualan_kredit')

    penjualan = models.penjualan2m.objects.filter(pk=id).first()
    return render(req, 'penjualan/edit_p_kredit.html', {
        'data': penjualan,
    })

def edit_p_kredit_terima(req, id):
    if req.POST:
        models.penjualan1m.objects.filter(pk=id).update(terima=req.POST['terima'])
        return redirect('/piutang')

    penjualan = models.penjualan1m.objects.filter(pk=id).first()
    return render(req, 'uangmasuk/edit_piutang.html', {
        'data': penjualan,
    })

def edit_p_kredit_terima1(req, id):
    if req.POST:
        models.penjualan3m.objects.filter(pk=id).update(terima=req.POST['terima'])
        return redirect('/piutang')

    penjualan = models.penjualan3m.objects.filter(pk=id).first()
    return render(req, 'uangmasuk/edit_piutang1.html', {
        'data1': penjualan,
    })

def edit_pend_lain_terima(req, id): 
    if req.POST:
        models.pend_lainm.objects.filter(pk=id).update(terima=req.POST['terima'])
        return redirect('/piutang')

    penjualan = models.pend_lainm.objects.filter(pk=id).first()
    return render(req, 'uangmasuk/edit_terimalain.html', {
        'data2': penjualan,
    })

def edit_p_lain(req, id):
    if req.POST:
        models.penjualan3m.objects.filter(pk=id).update(keterangan=req.POST['keterangan'], kas=req.POST['kas'], piutang=req.POST['piutang'], catatan=req.POST['catatan'])
        return redirect('/penjualan_lain')

    penjualan = models.penjualan3m.objects.filter(pk=id).first()
    return render(req, 'penjualan/edit_p_lain.html', {
        'data': penjualan,
    })

def edit_utang(req, id):
    if req.POST:
        models.utangm.objects.filter(pk=id).update(jumlah=req.POST['jumlah'], catatan=req.POST['catatan'])
        return redirect('/utang')

    utang = models.utangm.objects.filter(pk=id).first()
    return render(req, 'uangmasuk/edit_utang.html', {
        'data': utang,
    })

def edit_pend_lain(req, id):
    if req.POST:
        models.pend_lainm.objects.filter(pk=id).update(keterangan=req.POST['keterangan'], pendapatan=req.POST['pendapatan'], kas_masuk=req.POST['kas_masuk'])
        return redirect('/penjualan_tunai')

    pend = models.pend_lainm.objects.filter(pk=id).first()
    return render(req, 'uangmasuk/edit_pend_lain.html', {
        'data': pend,
    })

def edit_pem_tunai(req, id):
    if req.POST:
        models.pem_tunaim.objects.filter(pk=id).update(keterangan=req.POST['keterangan'], kas_keluar=req.POST['kas_keluar'])
        return redirect('/pembelian_tunai')

    pem = models.pem_tunaim.objects.filter(pk=id).first()
    return render(req, 'pembelian/edit_pem_tunai.html', {
        'data': pem,
    })

def edit_pem_kredit(req, id):
    if req.POST:
        models.pem_kreditm.objects.filter(pk=id).update(jumlah=req.POST['jumlah'], catatan=req.POST['catatan'])
        return redirect('/pembelian_kredit')

    pem = models.pem_kreditm.objects.filter(pk=id).first()
    return render(req, 'pembelian/edit_pem_kredit.html', {
        'data': pem,
    })

def edit_pem_lain(req, id):
    if req.POST:
        models.pem_lainm.objects.filter(pk=id).update(dibayar=req.POST['dibayar'], catatan=req.POST['catatan'])
        return redirect('/pembelian_lain')

    pem = models.pem_lainm.objects.filter(pk=id).first()
    return render(req, 'pembelian/edit_pem_lain.html', {
        'data': pem,
    })

def edit_pembayaran_biaya(req, id):
    if req.POST:
        models.pembayaran_biayam.objects.filter(pk=id).update(dibayar=req.POST['dibayar'], catatan=req.POST['catatan'])
        return redirect('/pembayaran_biaya')

    pem = models.pembayaran_biayam.objects.filter(pk=id).first()
    return render(req, 'uangkeluar/edit_pembayaran_biaya.html', {
        'data': pem,
    })

def edit_pembayaran_lain(req, id):
    if req.POST:
        models.pembayaran_lainm.objects.filter(pk=id).update(keterangan=req.POST['keterangan'], dibayar=req.POST['dibayar'], catatan=req.POST['catatan'])
        return redirect('/pembayaran_lain')

    pem = models.pembayaran_lainm.objects.filter(pk=id).first()
    return render(req, 'uangkeluar/edit_pembayaran_lain.html', {
        'data': pem,
    })

def edit_barang(req, id):
    if req.POST:
        models.barangm.objects.filter(pk=id).update(barang=req.POST['barang'], harga_beli=req.POST['harga_beli'], harga_jual=req.POST['harga_jual'])
        return redirect('/barang')

    pem = models.barangm.objects.filter(pk=id).first()
    return render(req, 'keperluan/edit_barang.html', {
        'data': pem,
    })

def edit_piutang(req, id):
    if req.POST:
        models.penjualan2m.objects.filter(pk=id).update(kuantitas=req.POST['kuantitas'], catatan=req.POST['catatan'])
        return redirect('/penjualan_kredit')

    penjualan = models.penjualan2m.objects.filter(pk=id).first()
    return render(req, 'penjualan/edit_p_kredit.html', {
        'data': penjualan,
    })

def edit_butang(req, id):
    if req.POST:
        models.utangm.objects.filter(pk=id).update(dibayar=req.POST['dibayar'])
        return redirect('/pembayaran_utang')

    utang = models.utangm.objects.filter(pk=id).first()
    return render(req, 'uangkeluar/edit_butang.html', {
        'data': utang,
    })

def edit_butang1(req, id):
    if req.POST:
        models.pem_kreditm.objects.filter(pk=id).update(dibayar1=req.POST['dibayar1'])
        return redirect('/pembayaran_utang')

    utang = models.pem_kreditm.objects.filter(pk=id).first()
    return render(req, 'uangkeluar/edit_butang1.html', {
        'data': utang,
    })

def edit_butang2(req, id):
    if req.POST:
        models.pem_lainm.objects.filter(pk=id).update(dibayar2=req.POST['dibayar2'])
        return redirect('/pembayaran_utang')

    utang = models.pem_lainm.objects.filter(pk=id).first()
    return render(req, 'uangkeluar/edit_butang2.html', {
        'data': utang,
    })

def edit_butang3(req, id):
    if req.POST:
        models.pem_tunaim.objects.filter(pk=id).update(dibayar=req.POST['dibayar'])
        return redirect('/pembayaran_utang')

    utang = models.pem_tunaim.objects.filter(pk=id).first()
    return render(req, 'uangkeluar/edit_butang3.html', {
        'data': utang,
    })

def edit_saldoawal(req, id):
    if req.POST:
        models.penjualan1m.objects.filter(pk=id).update(saldo_awal=req.POST['saldo_awal'])
        return redirect('/lr')

    penjualan = models.penjualan1m.objects.filter(pk=id).first()
    return render(req, 'keperluan/edit_saldo.html', {
        'data': penjualan,
    })


# Hapus
def hapus1(req, id):
    models.penjualan1m.objects.filter(pk=id).delete()
    return redirect('/penjualan_tunai')

def hapus2(req, id):
    models.penjualan2m.objects.filter(pk=id).delete()
    return redirect('/penjualan_kredit')

def hapus3(req, id):
    models.penjualan3m.objects.filter(pk=id).delete()
    return redirect('/penjualan_lain')

def hapus4(req, id):
    models.utangm.objects.filter(pk=id).delete()
    return redirect('/utang')

def hapus5(req, id):
    models.pem_tunaim.objects.filter(pk=id).delete()
    return redirect('/pembelian_tunai')

def hapus6(req, id):
    models.pem_kreditm.objects.filter(pk=id).delete()
    return redirect('/pembelian_tunai')

def hapus7(req, id):
    models.pem_lainm.objects.filter(pk=id).delete()
    return redirect('/pembelian_lain')

def hapus8(req, id):
    models.pembayaran_biayam.objects.filter(pk=id).delete()
    return redirect('/pembayaran_biaya')

def hapus9(req, id):
    models.pembayaran_lainm.objects.filter(pk=id).delete()
    return redirect('/pembayaran_lain')

def hapus10(req, id):
    models.pend_lainm.objects.filter(pk=id).delete()
    return redirect('/pend_lain')

def hapus11(req, id):
    models.barangm.objects.filter(pk=id).delete()
    return redirect('/barang')