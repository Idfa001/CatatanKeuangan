from django.shortcuts import render, redirect
from django.db.models import Sum
from bootstrap_datepicker_plus import DatePickerInput
from . import models, forms
from account.forms import CreateUserForm
from datetime import timedelta
from django.utils.timezone import now

def usaha(req):

    if not req.user.is_authenticated:
        return redirect ('/account')

    ush = models.usaha.objects.all()
    ush = models.usaha.objects.filter(owner=req.user)

    return render(req, 'crud/usaha1.html', {
    'data': ush,
    })

def notif_r(req, id):
    ush = models.usaha.objects.filter(pk=id).first()

    today = now().replace(hour=0, minute=0, second=0, microsecond=0)
    tomorrow = today + timedelta(days=10)
	
    notif = models.penjualan1m.objects.filter(
        usaha=ush,
        jatuh_tempo__gte=today,
        jatuh_tempo__lt=tomorrow,
    )

    notifnew = []
    for p in notif:
        if p.saldo() > 0:
            notifnew.append(p)
    
    return notifnew

def halamandepan(req, id):

 
    pen = models.penjualan1m.objects.all()
    pen2 = models.pend_lainm.objects.all()

    pen = models.penjualan1m.objects.filter(usaha=id)
    pen2 = models.pend_lainm.objects.filter(usaha=id)


    kas_masuk1 = 0
    for q in pen:
      kas_masuk1 += q.kas_masuk1()

    kas_masuk2 = 0
    for q in pen2:
      kas_masuk2 += q.jum_pend()

    penjualan1 = models.penjualan1m.objects.all()
    penjualan2 = models.pend_lainm.objects.all()

    penjualan1 = models.penjualan1m.objects.filter(usaha=id)
    penjualan2 = models.pend_lainm.objects.filter(usaha=id)

    total_terima1 = 0   

    for p in penjualan1:
      total_terima1 += p.terima

    total_terima2 = 0   

    for p in penjualan2:
      total_terima2 += p.terima

    kas_masuk3 = total_terima1 + total_terima2

    utang = models.utangm.objects.all()
    utang = models.utangm.objects.filter(usaha=id)

    kas_masuk4 = 0
    for i in utang:
      kas_masuk4 += i.jum_utang()

    pem = models.pem_tunaim.objects.all()
    pem1 = models.pem_kreditm.objects.all()

    pem = models.pem_tunaim.objects.filter(usaha=id)
    pem1 = models.pem_kreditm.objects.filter(usaha=id)

    kas_keluar1 = 0
    for i in pem:
      kas_keluar1 += i.kas_keluar1()

    kas_keluar2 = 0
    for i in pem1:
      kas_keluar2 += i.kas_keluar2()

    utang = models.utangm.objects.all()
    pem = models.pem_kreditm.objects.all()
    pem1 = models.pem_tunaim.objects.all()

    utang = models.utangm.objects.filter(usaha=id)
    pem = models.pem_kreditm.objects.filter(usaha=id)
    pem1 = models.pem_tunaim.objects.filter(usaha=id)


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

    pend = models.pend_lainm.objects.filter(usaha=id)
    penjualan1 = models.penjualan1m.objects.filter(usaha=id)
    penjualan2 = models.pend_lainm.objects.filter(usaha=id)

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

    utang = models.utangm.objects.filter(usaha=id)
    pem = models.pem_kreditm.objects.filter(usaha=id)
    pem1 = models.pem_tunaim.objects.filter(usaha=id)

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

    saldo_awal1 = models.SaldoAwal.objects.all()

    saldo_awal1 = models.SaldoAwal.objects.filter(usaha=id)

    saldo1 = 0
    for p in saldo_awal1:
        saldo1 += p.saldo_awal

    saldo_akhir = saldo1 + jumlah1 - jumlah2

    # persen
    pend = models.pend_lainm.objects.all()
    penjualan1 = models.penjualan1m.objects.all()
    penjualan2 = models.pend_lainm.objects.all()

    pend = models.pend_lainm.objects.filter(usaha=id)
    penjualan1 = models.penjualan1m.objects.filter(usaha=id)

    total_terima1 = 0   
    for p in penjualan1:
      total_terima1 += p.terima

    total_terima2 = 0   
    for p in pend:
      total_terima2 += p.terima

    saldo_total2 = total_terima1 + total_terima2

    penjualan1 = models.penjualan1m.objects.all()
    penjualan2 = models.pend_lainm.objects.all()
    
    penjualan1 = penjualan1.filter(usaha=id)
    penjualan2 = penjualan2.filter(usaha=id)

    piutang1 = 0
    for r in penjualan1:
      piutang1 += r.piutang1()

    jum_pend3 = 0
    for u in penjualan2:
      jum_pend3 += u.jum_pend3()

    saldo_total1 = piutang1 + jum_pend3

    persenpiutangxx = 0
    if not(saldo_total1 == 0):
        persenpiutangxx = saldo_total2 / saldo_total1 * 100
    persenpiutang = int(persenpiutangxx)

    # persenutang
    utang = models.utangm.objects.all()
    utang = models.utangm.objects.filter(usaha=id)

    jum_utang = 0
    for i in utang:
      jum_utang += i.jum_utang()

    pem = models.pem_tunaim.objects.all()
    pem1 = models.pem_kreditm.objects.all()

    pem = pem.filter(usaha=id)
    pem1 = pem1.filter(usaha=id)

    utang1 = 0
    for i in pem:
      utang1 += i.utang1()   

    utang2 = 0
    for i in pem1:
      utang2 += i.utang2() 

    jumlah_utang = jum_utang + utang1 + utang2

    utang = models.utangm.objects.all()
    pem = models.pem_kreditm.objects.all()
    pem1 = models.pem_tunaim.objects.all()

    utang = models.utangm.objects.filter(usaha=id)
    pem = models.pem_kreditm.objects.filter(usaha=id)
    pem1 = models.pem_tunaim.objects.filter(usaha=id)

    bayar11 = 0
    for p in pem:
        bayar11 += p.dibayar1
    
    bayar22 = 0
    for q in utang:
        bayar22 += q.dibayar
    
    bayar33 = 0
    for r in pem1:
        bayar33 += r.dibayar

    jumlahbayar = bayar11 + bayar22 + bayar33   

    persenutangcr = 0
    if not(jumlah_utang == 0):
        persenutangcr = jumlahbayar / jumlah_utang * 100 
    persenutang = int(persenutangcr)


    a = kas_masuk1 + kas_masuk2 - kas_keluar1 - kas_keluar2
    b = kas_masuk4 - kas_keluar3

    rasioxx = 0
    if not(b == 0):
        rasioxx = (a + kas_masuk3) / b *100
    rasio = int(rasioxx)

    saldo_awal1 = models.SaldoAwal.objects.all()
    saldo_awal1 = models.SaldoAwal.objects.filter(usaha=id)

    saldo1 = 0
    for p in saldo_awal1:
        saldo1 += p.saldo_awal

    c = kas_masuk1 + kas_masuk2 + kas_masuk3 + saldo1
    d = kas_keluar1 + kas_keluar2
    e = kas_masuk4 - kas_keluar3

    maks_keluar = c - d - e

    #usaha
    ush = models.usaha.objects.filter(pk=id).first()
    ush1 = models.usaha.objects.filter(owner=req.user)

    due = notif_r(req, id)
    

    return render(req, 'hal1/index1.html', {
    'id': id,
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
    'persenpiutang': persenpiutang,
    'persenutang': persenutang,
    'saldo_akhir': saldo_akhir,
    'rasio': rasio,
    'maks_keluar': maks_keluar,
    'data': ush1,
    'usaha': ush,
    'due': due,
    })

def penjualan_tunai(req, id):  
      
    if req.GET and req.GET["dari"] and req.GET["sampai"]: 
        penjualan1 = models.penjualan1m.objects.filter(tanggal__range=[req.GET["dari"], req.GET["sampai"]])
        penjualan2 = models.pend_lainm.objects.filter(tanggal__range=[req.GET["dari"], req.GET["sampai"]])
 
    else:
        penjualan1 = models.penjualan1m.objects.all()
        penjualan2 = models.pend_lainm.objects.all()
    
    penjualan1 = penjualan1.filter(usaha=id)
    penjualan2 = penjualan2.filter(usaha=id)
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
        'id': id,
        'data': penjualan1,
        'data1': penjualan2,
        'jum_pend1':jum_pend1,
        'jum_pend': jum_pend,
        'jum_pend3':jum_pend3,
        'kas_masuk1': kas_masuk1,
        'piutang1': piutang1,
        'total': total,
    })

def piutang(req, id):
    pend = models.pend_lainm.objects.all()
    penjualan1 = models.penjualan1m.objects.all()
    penjualan2 = models.pend_lainm.objects.all()

    pend = models.pend_lainm.objects.filter(usaha=id)
    penjualan1 = models.penjualan1m.objects.filter(usaha=id)
    penjualan2 = models.pend_lainm.objects.filter(usaha=id)

    penjualan1new = []
    for p in penjualan1:
        if p.saldo() > 0:
            penjualan1new.append(p)

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
        'id': id,
        'data2': pend,
        'data' :penjualan1new,
        'data1' :penjualan2,
        'saldo_total1': saldo_total1,
        'saldo_total2': saldo_total2,
        
    })

def utang(req, id):
    task = models.utangm.objects.filter(usaha=id)
    form_input = forms.utangf()
    if req.POST:
        form_input = forms.utangf(req.POST)
        if form_input.is_valid():
            form_input.instance.usaha = usaha
            form_input.save()
        return redirect('/utang')

    utang = models.utangm.objects.all()
    utang = models.utangm.objects.filter(usaha=id)

    jum_utang = 0
    for i in utang:
      jum_utang += i.jum_utang()

    return render(req, 'uangmasuk/index7.html', {
        'id': id,
        'data': utang,
        'data': task,
        'jum_utang': jum_utang,
        'form': form_input,        
    })

def pembelian_tunai(req, id):
    task = models.pem_tunaim.objects.filter(usaha=id)
    form_input = forms.pem_tunaif()
    if req.POST:
        form_input = forms.pem_tunaif(req.POST, usaha=id)
        if form_input.is_valid():
            form_input.instance.usaha = usaha
            form_input.save()
        return redirect('/pembelian_tunai')
    pem = models.pem_tunaim.objects.all()
    pem1 = models.pem_kreditm.objects.all()

    pem = pem.filter(usaha=id)
    pem1 = pem1.filter(usaha=id)

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
        'id': id,
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




def pembayaran_utang(req, id):
    
    utang = models.utangm.objects.all()
    pem = models.pem_kreditm.objects.all()
    pem1 = models.pem_tunaim.objects.all()

    utang = models.utangm.objects.filter(usaha=id)
    pem = models.pem_kreditm.objects.filter(usaha=id)
    pem1 = models.pem_tunaim.objects.filter(usaha=id)

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
        'id': id,
        'data': utang,
        'data1': pem,
        'data2': pem1,
        'jumlah1' : jumlah1,
        'jumlah2' : jumlah2,
    })

 

def barang(req, id):
    task = models.barangm.objects.filter(usaha=id)
    form_input = forms.barangf()
    if req.POST:
        form_input = forms.barangf(req.POST)
        if form_input.is_valid():
            form_input.instance.usaha = usaha
            form_input.save()
        return redirect('/barang')
    return render(req, 'keperluan/index18.html', {
        'id': id,
        'data': task,
        'form': form_input,
    })

def lr(req, id):
    usaha = models.usaha.objects.filter(pk=id).first()
    saldo_awal = models.SaldoAwal.objects.filter(usaha=id).first()
    if  req.POST:


        if saldo_awal:
            models.SaldoAwal.objects.filter(usaha=id).update(saldo_awal=req.POST['saldo_awal'])
        else:
            models.SaldoAwal.objects.create(saldo_awal=req.POST['saldo_awal'], usaha=usaha)

        return redirect(f'/usaha/lr/{id}') 





    pen = models.penjualan1m.objects.all()
    pen2 = models.pend_lainm.objects.all()

    pen = models.penjualan1m.objects.filter(usaha=id)
    pen2 = models.pend_lainm.objects.filter(usaha=id)

    kas_masuk1 = 0
    for q in pen:
      kas_masuk1 += q.kas_masuk1()

    kas_masuk2 = 0
    for q in pen2:
      kas_masuk2 += q.jum_pend()

    penjualan1 = models.penjualan1m.objects.all()
    penjualan2 = models.pend_lainm.objects.all()

    penjualan1 = models.penjualan1m.objects.filter(usaha=id)
    penjualan2 = models.pend_lainm.objects.filter(usaha=id)

    total_terima1 = 0   

    for p in penjualan1:
      total_terima1 += p.terima

    total_terima2 = 0   

    for p in penjualan2:
      total_terima2 += p.terima

    kas_masuk3 = total_terima1 + total_terima2

    utang = models.utangm.objects.all()

    utang = models.utangm.objects.filter(usaha=id)

    kas_masuk4 = 0
    for i in utang:
      kas_masuk4 += i.jum_utang()

    pem = models.pem_tunaim.objects.all()
    pem1 = models.pem_kreditm.objects.all()

    pem = models.pem_tunaim.objects.filter(usaha=id)
    pem1 = models.pem_kreditm.objects.filter(usaha=id)

    kas_keluar1 = 0
    for i in pem:
      kas_keluar1 += i.kas_keluar1()

    kas_keluar2 = 0
    for i in pem1:
      kas_keluar2 += i.kas_keluar2()

    utang = models.utangm.objects.all()
    pem = models.pem_kreditm.objects.all()
    pem1 = models.pem_tunaim.objects.all()

    utang = models.utangm.objects.filter(usaha=id)
    pem = models.pem_kreditm.objects.filter(usaha=id)
    pem1 = models.pem_tunaim.objects.filter(usaha=id)

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

    saldo_awal1 = models.SaldoAwal.objects.all()

    saldo_awal1 = models.SaldoAwal.objects.filter(usaha=id)

    saldo1 = 0
    for p in saldo_awal1:
        saldo1 += p.saldo_awal

    saldo = saldo1 + total
       
    return render(req, 'keperluan/index16.html', {
    'id': id,
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

def penjualan1v(req, id):
    usaha = models.usaha.objects.filter(pk=id).first()
    task = models.penjualan1m.objects.filter(usaha=id)
    form_input = forms.penjualan1f(usaha=id)
    if req.POST:
        form_input = forms.penjualan1f(req.POST, usaha=id)
        if form_input.is_valid():
            form_input.instance.usaha = usaha
            form_input.save()
        return redirect(f'/usaha/penjualan_tunai/{id}')
    return render(req, 'crud/penjualan1.html', {
        'id': id,
        'form': form_input,
        'data': task,
    })



def utangv(req, id):
    usaha = models.usaha.objects.filter(pk=id).first()
    task = models.barangm.objects.filter(usaha=id)
    form_input = forms.utangf()
    if req.POST:
        form_input = forms.utangf(req.POST)
        if form_input.is_valid():
            form_input.instance.usaha = usaha
            form_input.save()
        return redirect(f'/usaha/utang/{id}')
    return render(req, 'crud/utang.html', {
        'id': id,
        'form': form_input,
        'data': task,
    })

def pend_lainv(req, id):
    usaha = models.usaha.objects.filter(pk=id).first()
    task = models.pend_lainm.objects.filter(usaha=id)
    form_input = forms.pend_lainf()
    if req.POST:
        form_input = forms.pend_lainf(req.POST)
        if form_input.is_valid():
            form_input.instance.usaha = usaha
            form_input.save()
        return redirect(f'/usaha/penjualan_tunai/{id}')
    return render(req, 'crud/pend_lain.html', {
        'id': id,
        'form': form_input,
        'data': task,
    })

def pem_tunaiv(req, id):
    usaha = models.usaha.objects.filter(pk=id).first()
    task = models.barangm.objects.filter(usaha=id)
    form_input = forms.pem_tunaif()
    if req.POST:
        form_input = forms.pem_tunaif(req.POST)
        if form_input.is_valid():
            form_input.instance.usaha = usaha
            form_input.save()
        return redirect(f'/usaha/pembelian_tunai/{id}')
    return render(req, 'crud/pem_tunai.html', {
        'id': id,
        'form': form_input,
        'data': task,
    })

def pem_kreditv(req, id):
    usaha = models.usaha.objects.filter(pk=id).first()
    task = models.pem_kreditm.objects.filter(usaha=id)
    form_input = forms.pem_kreditf(usaha=id)
    if req.POST:
        form_input = forms.pem_kreditf(req.POST, usaha=id)
        if form_input.is_valid():
            form_input.instance.usaha = usaha
            form_input.save()
        return redirect(f'/usaha/pembelian_tunai/{id}')
    return render(req, 'crud/pem_kredit.html', {
        'id': id,
        'form': form_input,
        'data': task,
    })

def pem_lainv(req, id):
    usaha = models.usaha.objects.filter(pk=id).first()
    task = models.barangm.objects.filter(usaha=id)
    form_input = forms.pem_lainf()
    if req.POST:
        form_input = forms.pem_lainf(req.POST)
        if form_input.is_valid():
            form_input.instance.usaha = usaha
            form_input.save()
        return redirect('/pembelian_lain')
    return render(req, 'crud/pem_lain.html', {
        'id': id,
        'form': form_input,
        'data': task,
    })


def barangv(req, id):
    usaha = models.usaha.objects.filter(pk=id).first()
    form_input = forms.barangf()
    if req.POST:
        form_input = forms.barangf(req.POST)
        if form_input.is_valid():
            form_input.instance.usaha = usaha
            form_input.save()
        return redirect(f'/usaha/barang/{id}') 
    return render(req, 'crud/barang.html', {
        'id': id,
        'form': form_input,
    })


def usahav(req):
    form_input = forms.usahaf()
    if req.POST:
        form_input = forms.usahaf(req.POST)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
        return redirect('/usaha')
    return render(req, 'crud/usaha.html', {
        'form': form_input,
    })

#bayar
def penjualan1bayar(req, id):
    usaha = models.usaha.objects.filter(pk=id).first()
    if req.POST:
        models.penjualan1m.objects.filter(pk=id_p).update(kuantitas=req.POST['kuantitas'], kas_masuk=req.POST['kas_masuk'])
        return redirect(f'/usaha/penjualan1bayar/{id}')
    penjualan = models.penjualan1m.objects.filter(pk=id).first()
    return render(req, 'crud/penjualan1bayar.html', {
        'id': id,
        'data': penjualan,
    })

# def penjualan1bayar(req, id, id_p):
#     if req.POST:
#         models.penjualan1m.objects.filter(pk=id_p).update(kuantitas=req.POST['kuantitas'], kas_masuk=req.POST['kas_masuk'])
#         return redirect(f'/usaha/penjualan_tunai/{id}')
#     penjualan1 = models.penjualan1m.objects.all()    
#     penjualan1 = penjualan1.filter(usaha=id)
#     # penjualan = models.penjualan1m.objects.filter(pk=id_p).first()
#     return render(req, 'crud/penjualan1bayar.html', {
#         'id': id,
#         'data': penjualan1,
#     })

 


#edit
def edit_p_tunai(req, id, id_p):
    if req.POST:
        models.penjualan1m.objects.filter(pk=id_p).update(kuantitas=req.POST['kuantitas'], kas_masuk=req.POST['kas_masuk'])
        return redirect(f'/usaha/penjualan_tunai/{id}')

    penjualan = models.penjualan1m.objects.filter(pk=id).first()
    return render(req, 'penjualan/edit_p_tunai.html', {
        'data': penjualan,
    })

def edit_p_kredit(req, id, id_p):
    if req.POST:
        models.penjualan2m.objects.filter(pk=id_p).update(kuantitas=req.POST['kuantitas'], catatan=req.POST['catatan'], jatuh_tempo=req.POST['jatuh_tempo'])
        return redirect(f'/usaha/penjualan_kredit/{id}')

    penjualan = models.penjualan2m.objects.filter(pk=id).first()
    return render(req, 'penjualan/edit_p_kredit.html', {
        'data': penjualan,
    })

def edit_p_kredit_terima(req, id, id_p):
    if req.POST:
        models.penjualan1m.objects.filter(pk=id_p).update(terima=req.POST['terima'])
        return redirect(f'/usaha/piutang/{id}')

    penjualan = models.penjualan1m.objects.filter(pk=id).first()
    return render(req, 'uangmasuk/edit_piutang.html', {
        'data': penjualan,
    })

def edit_p_kredit_terima1(req, id, id_p):
    if req.POST:
        models.penjualan3m.objects.filter(pk=id_p).update(terima=req.POST['terima'])
        return redirect(f'/usaha/piutang/{id}')

    penjualan = models.penjualan3m.objects.filter(pk=id).first()
    return render(req, 'uangmasuk/edit_piutang1.html', {
        'data1': penjualan,
    })

def edit_pend_lain_terima(req, id, id_p): 
    if req.POST:
        models.pend_lainm.objects.filter(pk=id_p).update(terima=req.POST['terima'])
        return redirect(f'/usaha/piutang/{id}')

    penjualan = models.pend_lainm.objects.filter(pk=id).first()
    return render(req, 'uangmasuk/edit_terimalain.html', {
        'data2': penjualan,
    })

def edit_p_lain(req, id, id_p):
    if req.POST:
        models.penjualan3m.objects.filter(pk=id_p).update(keterangan=req.POST['keterangan'], kas=req.POST['kas'], piutang=req.POST['piutang'], catatan=req.POST['catatan'])
        return redirect(f'/usaha/penjualan_lain/{id}')

    penjualan = models.penjualan3m.objects.filter(pk=id).first()
    return render(req, 'penjualan/edit_p_lain.html', {
        'data': penjualan,
    })

def edit_utang(req, id, id_p):
    if req.POST:
        models.utangm.objects.filter(pk=id_p).update(jumlah=req.POST['jumlah'], catatan=req.POST['catatan'])
        return redirect(f'/usaha/utang/{id}')

    utang = models.utangm.objects.filter(pk=id).first()
    return render(req, 'uangmasuk/edit_utang.html', {
        'data': utang,
    })

def edit_pend_lain(req, id, id_p):
    if req.POST:
        models.pend_lainm.objects.filter(pk=id_p).update(keterangan=req.POST['keterangan'], pendapatan=req.POST['pendapatan'], kas_masuk=req.POST['kas_masuk'])
        return redirect(f'/usaha/penjualan_tunai/{id}')

    pend = models.pend_lainm.objects.filter(pk=id).first()
    return render(req, 'uangmasuk/edit_pend_lain.html', {
        'data': pend,
    })

def edit_pem_tunai(req, id, id_p):
    if req.POST:
        models.pem_tunaim.objects.filter(pk=id_p).update(keterangan=req.POST['keterangan'], kas_keluar=req.POST['kas_keluar'])
        return redirect(f'/usaha/pembelian_tunai/{id}')

    pem = models.pem_tunaim.objects.filter(pk=id).first()
    return render(req, 'pembelian/edit_pem_tunai.html', {
        'data': pem,
    })

def edit_pem_kredit(req, id, id_p):
    if req.POST:
        models.pem_kreditm.objects.filter(pk=id_p).update(jumlah=req.POST['jumlah'], catatan=req.POST['catatan'])
        return redirect(f'/usaha/pembelian_kredit/{id}')

    pem = models.pem_kreditm.objects.filter(pk=id).first()
    return render(req, 'pembelian/edit_pem_kredit.html', {
        'data': pem,
    })

def edit_pem_lain(req, id, id_p):
    if req.POST:
        models.pem_lainm.objects.filter(pk=id_p).update(dibayar=req.POST['dibayar'], catatan=req.POST['catatan'])
        return redirect(f'/usaha/pembelian_lain/{id}')

    pem = models.pem_lainm.objects.filter(pk=id).first()
    return render(req, 'pembelian/edit_pem_lain.html', {
        'data': pem,
    })

def edit_pembayaran_biaya(req, id, id_p):
    if req.POST:
        models.pembayaran_biayam.objects.filter(pk=id_p).update(dibayar=req.POST['dibayar'], catatan=req.POST['catatan'])
        return redirect(f'/usaha/pembayaran_biaya/{id}')

    pem = models.pembayaran_biayam.objects.filter(pk=id).first()
    return render(req, 'uangkeluar/edit_pembayaran_biaya.html', {
        'data': pem,
    })

def edit_pembayaran_lain(req, id, id_p):
    if req.POST:
        models.pembayaran_lainm.objects.filter(pk=id_p).update(keterangan=req.POST['keterangan'], dibayar=req.POST['dibayar'], catatan=req.POST['catatan'])
        return redirect(f'/usaha/pembayaran_lain/{id}')

    pem = models.pembayaran_lainm.objects.filter(pk=id).first()
    return render(req, 'uangkeluar/edit_pembayaran_lain.html', {
        'data': pem,
    })

def edit_barang(req, id, id_p):
    if req.POST:
        models.barangm.objects.filter(pk=id_p).update(barang=req.POST['barang'], harga_beli=req.POST['harga_beli'], harga_jual=req.POST['harga_jual'])
        return redirect(f'/usaha/barang/{id}')

    pem = models.barangm.objects.filter(pk=id).first()
    return render(req, 'keperluan/edit_barang.html', {
        'data': pem,
    })

def edit_piutang(req, id, id_p):
    if req.POST:
        models.penjualan2m.objects.filter(pk=id_p).update(kuantitas=req.POST['kuantitas'], catatan=req.POST['catatan'])
        return redirect(f'/usaha/penjualan_kredit/{id}')

    penjualan = models.penjualan2m.objects.filter(pk=id).first()
    return render(req, 'penjualan/edit_p_kredit.html', {
        'data': penjualan,
    })

def edit_butang(req, id, id_p):
    if req.POST:
        models.utangm.objects.filter(pk=id_p).update(dibayar=req.POST['dibayar'])
        return redirect(f'/usaha/pembayaran_utang/{id}')

    utang = models.utangm.objects.filter(pk=id).first()
    return render(req, 'uangkeluar/edit_butang.html', {
        'data': utang,
    })

def edit_butang1(req, id, id_p):
    if req.POST:
        models.pem_kreditm.objects.filter(pk=id_p).update(dibayar1=req.POST['dibayar1'])
        return redirect(f'/usaha/pembayaran_utang/{id}')

    utang = models.pem_kreditm.objects.filter(pk=id).first()
    return render(req, 'uangkeluar/edit_butang1.html', {
        'data': utang,
    })

def edit_butang2(req, id, id_p):
    if req.POST:
        models.pem_lainm.objects.filter(pk=id_p).update(dibayar2=req.POST['dibayar2'])
        return redirect(f'/usaha/pembayaran_utang/{id}')

    utang = models.pem_lainm.objects.filter(pk=id).first()
    return render(req, 'uangkeluar/edit_butang2.html', {
        'data': utang,
    })

def edit_butang3(req, id, id_p):
    if req.POST:
        models.pem_tunaim.objects.filter(pk=id_p).update(dibayar=req.POST['dibayar'])
        return redirect(f'/usaha/pembayaran_utang/{id}')

    utang = models.pem_tunaim.objects.filter(pk=id).first()
    return render(req, 'uangkeluar/edit_butang3.html', {
        'data': utang,
    })

def edit_saldoawal(req, id, id_p):
    if req.POST:
        models.penjualan1m.objects.filter(pk=id_p).update(saldo_awal=req.POST['saldo_awal'])
        return redirect(f'/usaha/lr/{id}')

    penjualan = models.penjualan1m.objects.filter(pk=id).first()
    return render(req, 'keperluan/edit_saldo.html', {
        'data': penjualan,
    })

def edit_usaha(req, id):
    if req.POST:
        models.usaha.objects.filter(pk=id).update(nama_usaha=req.POST['nama_usaha'], alamat_usaha=req.POST['alamat_usaha'], jenis_usaha=req.POST['jenis_usaha'])
        return redirect('/usaha')

    ush = models.usaha.objects.filter(pk=id).first()
    return render(req, 'keperluan/edit_usaha.html', {
        'data': ush,
    })


# Hapus
def hapus1(req, id, id_p):
    models.penjualan1m.objects.filter(pk=id_p).delete()
    return redirect(f'/usaha/penjualan_tunai/{id}')

def hapus2(req, id, id_p):
    models.penjualan2m.objects.filter(pk=id_p).delete()
    return redirect(f'/usaha/penjualan_kredit/{id}')

def hapus3(req, id, id_p):
    models.penjualan3m.objects.filter(pk=id_p).delete()
    return redirect(f'/usaha/penjualan_lain/{id}')

def hapus4(req, id, id_p):
    models.utangm.objects.filter(pk=id_p).delete()
    return redirect(f'/usaha/utang/{id}')

def hapus5(req, id, id_p):
    models.pem_tunaim.objects.filter(pk=id_p).delete()
    return redirect(f'/usaha/pembelian_tunai/{id}')

def hapus6(req, id, id_p):
    models.pem_kreditm.objects.filter(pk=id_p).delete()
    return redirect(f'/usaha/pembelian_tunai/{id}')

def hapus7(req, id, id_p):
    models.pem_lainm.objects.filter(pk=id_p).delete()
    return redirect(f'/usaha/pembelian_lain/{id}')

def hapus8(req, id, id_p):
    models.pembayaran_biayam.objects.filter(pk=id_p).delete()
    return redirect(f'/usaha/pembayaran_biaya/{id}')

def hapus9(req, id, id_p):
    models.pembayaran_lainm.objects.filter(pk=id_p).delete()
    return redirect(f'/usaha/pembayaran_lain/{id}')

def hapus10(req, id, id_p):
    models.pend_lainm.objects.filter(pk=id_p).delete()
    return redirect(f'/usaha/penjualan_tunai/{id}')

def hapus11(req, id, id_p):
    models.barangm.objects.filter(pk=id_p).delete()
    return redirect(f'/usaha/barang/{id}')

def hapus12(req, id):
    models.usaha.objects.filter(pk=id).delete()
    return redirect('/usaha')


# wia
def wia(req, id):
    pen = models.penjualan1m.objects.all()
    pen2 = models.pend_lainm.objects.all()

    pen = models.penjualan1m.objects.filter(usaha=id)
    pen2 = models.pend_lainm.objects.filter(usaha=id)

    kas_masuk1 = 0
    for q in pen:
      kas_masuk1 += q.kas_masuk1()

    kas_masuk2 = 0
    for q in pen2:
      kas_masuk2 += q.jum_pend()

    penjualan1 = models.penjualan1m.objects.all()
    penjualan2 = models.pend_lainm.objects.all()

    penjualan1 = models.penjualan1m.objects.filter(usaha=id)
    penjualan2 = models.pend_lainm.objects.filter(usaha=id)

    total_terima1 = 0   

    for p in penjualan1:
      total_terima1 += p.terima

    total_terima2 = 0   

    for p in penjualan2:
      total_terima2 += p.terima

    kas_masuk3 = total_terima1 + total_terima2

    utang = models.utangm.objects.all()

    utang = models.utangm.objects.filter(usaha=id)

    kas_masuk4 = 0
    for i in utang:
      kas_masuk4 += i.jum_utang()

    pem = models.pem_tunaim.objects.all()
    pem1 = models.pem_kreditm.objects.all()

    pem = models.pem_tunaim.objects.filter(usaha=id)
    pem1 = models.pem_kreditm.objects.filter(usaha=id)

    kas_keluar1 = 0
    for i in pem:
      kas_keluar1 += i.kas_keluar1()

    kas_keluar2 = 0
    for i in pem1:
      kas_keluar2 += i.kas_keluar2()

    utang = models.utangm.objects.all()
    pem = models.pem_kreditm.objects.all()
    pem1 = models.pem_tunaim.objects.all()

    utang = models.utangm.objects.filter(usaha=id)
    pem = models.pem_kreditm.objects.filter(usaha=id)
    pem1 = models.pem_tunaim.objects.filter(usaha=id)

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

    saldo_awal1 = models.SaldoAwal.objects.all()

    saldo_awal1 = models.SaldoAwal.objects.filter(usaha=id)

       
    return render(req, 'keperluan/index17.html', {
    'id': id,
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
    })

def wia10(req, id):
    pen = models.penjualan1m.objects.all()
    pen2 = models.pend_lainm.objects.all()

    pen = models.penjualan1m.objects.filter(usaha=id)
    pen2 = models.pend_lainm.objects.filter(usaha=id)

    kas_masuk1 = 0
    for q in pen:
      kas_masuk1 += q.kas_masuk1() + (q.kas_masuk1() * 10 / 100)

    kas_masuk2 = 0
    for q in pen2:
      kas_masuk2 += q.jum_pend() + (q.jum_pend() * 10 / 100)

    penjualan1 = models.penjualan1m.objects.all()
    penjualan2 = models.pend_lainm.objects.all()

    penjualan1 = models.penjualan1m.objects.filter(usaha=id)
    penjualan2 = models.pend_lainm.objects.filter(usaha=id)

    total_terima1 = 0   

    for p in penjualan1:
      total_terima1 += p.terima 

    total_terima2 = 0   

    for p in penjualan2:
      total_terima2 += p.terima

    kas_masuk3 = ((total_terima1 + total_terima2) * 10 / 100) + (total_terima1 + total_terima2)

    utang = models.utangm.objects.all()

    utang = models.utangm.objects.filter(usaha=id)

    kas_masuk4 = 0
    for i in utang:
      kas_masuk4 += i.jum_utang() + (i.jum_utang() * 10 / 100)

    pem = models.pem_tunaim.objects.all()
    pem1 = models.pem_kreditm.objects.all()

    pem = models.pem_tunaim.objects.filter(usaha=id)
    pem1 = models.pem_kreditm.objects.filter(usaha=id)

    kas_keluar1 = 0
    for i in pem:
      kas_keluar1 += i.kas_keluar1() + (i.kas_keluar1() * 10 / 100)

    kas_keluar2 = 0
    for i in pem1:
      kas_keluar2 += i.kas_keluar2() + (i.kas_keluar2() * 10 / 100)

    utang = models.utangm.objects.all()
    pem = models.pem_kreditm.objects.all()
    pem1 = models.pem_tunaim.objects.all()

    utang = models.utangm.objects.filter(usaha=id)
    pem = models.pem_kreditm.objects.filter(usaha=id)
    pem1 = models.pem_tunaim.objects.filter(usaha=id)

    bayar11 = 0

    for p in pem:
        bayar11 += p.dibayar1
    
    bayar22 = 0

    for q in utang:
        bayar22 += q.dibayar
    
    bayar33 = 0

    for r in pem1:
        bayar33 += r.dibayar

    kas_keluar3 = (bayar11 + bayar22 + bayar33) + ((bayar11 + bayar22 + bayar33) * 10 / 100)

    jumlah1 = kas_masuk1 + kas_masuk2 + kas_masuk3 + kas_masuk4
    jumlah2 = kas_keluar1 + kas_keluar2 + kas_keluar3

    total = jumlah1 - jumlah2

    saldo_awal1 = models.SaldoAwal.objects.all()

    saldo_awal1 = models.SaldoAwal.objects.filter(usaha=id)

       
    return render(req, 'wia/wia10.html', {
    'id': id,
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
    })

def wia25(req, id):
    pen = models.penjualan1m.objects.all()
    pen2 = models.pend_lainm.objects.all()

    pen = models.penjualan1m.objects.filter(usaha=id)
    pen2 = models.pend_lainm.objects.filter(usaha=id)

    kas_masuk1 = 0
    for q in pen:
      kas_masuk1 += q.kas_masuk1() + (q.kas_masuk1() * 25 / 100)

    kas_masuk2 = 0
    for q in pen2:
      kas_masuk2 += q.jum_pend() + (q.jum_pend() * 25 / 100)

    penjualan1 = models.penjualan1m.objects.all()
    penjualan2 = models.pend_lainm.objects.all()

    penjualan1 = models.penjualan1m.objects.filter(usaha=id)
    penjualan2 = models.pend_lainm.objects.filter(usaha=id)

    total_terima1 = 0   

    for p in penjualan1:
      total_terima1 += p.terima 

    total_terima2 = 0   

    for p in penjualan2:
      total_terima2 += p.terima

    kas_masuk3 = ((total_terima1 + total_terima2) * 25 / 100) + (total_terima1 + total_terima2)

    utang = models.utangm.objects.all()

    utang = models.utangm.objects.filter(usaha=id)

    kas_masuk4 = 0
    for i in utang:
      kas_masuk4 += i.jum_utang() + (i.jum_utang() * 25 / 100)

    pem = models.pem_tunaim.objects.all()
    pem1 = models.pem_kreditm.objects.all()

    pem = models.pem_tunaim.objects.filter(usaha=id)
    pem1 = models.pem_kreditm.objects.filter(usaha=id)

    kas_keluar1 = 0
    for i in pem:
      kas_keluar1 += i.kas_keluar1() + (i.kas_keluar1() * 25 / 100)

    kas_keluar2 = 0
    for i in pem1:
      kas_keluar2 += i.kas_keluar2() + (i.kas_keluar2() * 25 / 100)

    utang = models.utangm.objects.all()
    pem = models.pem_kreditm.objects.all()
    pem1 = models.pem_tunaim.objects.all()

    utang = models.utangm.objects.filter(usaha=id)
    pem = models.pem_kreditm.objects.filter(usaha=id)
    pem1 = models.pem_tunaim.objects.filter(usaha=id)

    bayar11 = 0

    for p in pem:
        bayar11 += p.dibayar1
    
    bayar22 = 0

    for q in utang:
        bayar22 += q.dibayar
    
    bayar33 = 0

    for r in pem1:
        bayar33 += r.dibayar

    kas_keluar3 = (bayar11 + bayar22 + bayar33) + ((bayar11 + bayar22 + bayar33) * 25 / 100)

    jumlah1 = kas_masuk1 + kas_masuk2 + kas_masuk3 + kas_masuk4
    jumlah2 = kas_keluar1 + kas_keluar2 + kas_keluar3

    total = jumlah1 - jumlah2

    saldo_awal1 = models.SaldoAwal.objects.all()

    saldo_awal1 = models.SaldoAwal.objects.filter(usaha=id)

       
    return render(req, 'wia/wia25.html', {
    'id': id,
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
    })

def wia50(req, id):
    pen = models.penjualan1m.objects.all()
    pen2 = models.pend_lainm.objects.all()

    pen = models.penjualan1m.objects.filter(usaha=id)
    pen2 = models.pend_lainm.objects.filter(usaha=id)

    kas_masuk1 = 0
    for q in pen:
      kas_masuk1 += q.kas_masuk1() + (q.kas_masuk1() * 50 / 100)

    kas_masuk2 = 0
    for q in pen2:
      kas_masuk2 += q.jum_pend() + (q.jum_pend() * 50 / 100)

    penjualan1 = models.penjualan1m.objects.all()
    penjualan2 = models.pend_lainm.objects.all()

    penjualan1 = models.penjualan1m.objects.filter(usaha=id)
    penjualan2 = models.pend_lainm.objects.filter(usaha=id)

    total_terima1 = 0   

    for p in penjualan1:
      total_terima1 += p.terima 

    total_terima2 = 0   

    for p in penjualan2:
      total_terima2 += p.terima

    kas_masuk3 = ((total_terima1 + total_terima2) * 50 / 100) + (total_terima1 + total_terima2)

    utang = models.utangm.objects.all()

    utang = models.utangm.objects.filter(usaha=id)

    kas_masuk4 = 0
    for i in utang:
      kas_masuk4 += i.jum_utang() + (i.jum_utang() * 50 / 100)

    pem = models.pem_tunaim.objects.all()
    pem1 = models.pem_kreditm.objects.all()

    pem = models.pem_tunaim.objects.filter(usaha=id)
    pem1 = models.pem_kreditm.objects.filter(usaha=id)

    kas_keluar1 = 0
    for i in pem:
      kas_keluar1 += i.kas_keluar1() + (i.kas_keluar1() * 50 / 100)

    kas_keluar2 = 0
    for i in pem1:
      kas_keluar2 += i.kas_keluar2() + (i.kas_keluar2() * 50 / 100)

    utang = models.utangm.objects.all()
    pem = models.pem_kreditm.objects.all()
    pem1 = models.pem_tunaim.objects.all()

    utang = models.utangm.objects.filter(usaha=id)
    pem = models.pem_kreditm.objects.filter(usaha=id)
    pem1 = models.pem_tunaim.objects.filter(usaha=id)

    bayar11 = 0

    for p in pem:
        bayar11 += p.dibayar1
    
    bayar22 = 0

    for q in utang:
        bayar22 += q.dibayar
    
    bayar33 = 0

    for r in pem1:
        bayar33 += r.dibayar

    kas_keluar3 = (bayar11 + bayar22 + bayar33) + ((bayar11 + bayar22 + bayar33) * 50 / 100)

    jumlah1 = kas_masuk1 + kas_masuk2 + kas_masuk3 + kas_masuk4
    jumlah2 = kas_keluar1 + kas_keluar2 + kas_keluar3

    total = jumlah1 - jumlah2

    saldo_awal1 = models.SaldoAwal.objects.all()

    saldo_awal1 = models.SaldoAwal.objects.filter(usaha=id)

       
    return render(req, 'wia/wia50.html', {
    'id': id,
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
    })

def wia75(req, id):
    pen = models.penjualan1m.objects.all()
    pen2 = models.pend_lainm.objects.all()

    pen = models.penjualan1m.objects.filter(usaha=id)
    pen2 = models.pend_lainm.objects.filter(usaha=id)

    kas_masuk1 = 0
    for q in pen:
      kas_masuk1 += q.kas_masuk1() + (q.kas_masuk1() * 75 / 100)

    kas_masuk2 = 0
    for q in pen2:
      kas_masuk2 += q.jum_pend() + (q.jum_pend() * 75 / 100)

    penjualan1 = models.penjualan1m.objects.all()
    penjualan2 = models.pend_lainm.objects.all()

    penjualan1 = models.penjualan1m.objects.filter(usaha=id)
    penjualan2 = models.pend_lainm.objects.filter(usaha=id)

    total_terima1 = 0   

    for p in penjualan1:
      total_terima1 += p.terima 

    total_terima2 = 0   

    for p in penjualan2:
      total_terima2 += p.terima

    kas_masuk3 = ((total_terima1 + total_terima2) * 75 / 100) + (total_terima1 + total_terima2)

    utang = models.utangm.objects.all()

    utang = models.utangm.objects.filter(usaha=id)

    kas_masuk4 = 0
    for i in utang:
      kas_masuk4 += i.jum_utang() + (i.jum_utang() * 75 / 100)

    pem = models.pem_tunaim.objects.all()
    pem1 = models.pem_kreditm.objects.all()

    pem = models.pem_tunaim.objects.filter(usaha=id)
    pem1 = models.pem_kreditm.objects.filter(usaha=id)

    kas_keluar1 = 0
    for i in pem:
      kas_keluar1 += i.kas_keluar1() + (i.kas_keluar1() * 75 / 100)

    kas_keluar2 = 0
    for i in pem1:
      kas_keluar2 += i.kas_keluar2() + (i.kas_keluar2() * 75 / 100)

    utang = models.utangm.objects.all()
    pem = models.pem_kreditm.objects.all()
    pem1 = models.pem_tunaim.objects.all()

    utang = models.utangm.objects.filter(usaha=id)
    pem = models.pem_kreditm.objects.filter(usaha=id)
    pem1 = models.pem_tunaim.objects.filter(usaha=id)

    bayar11 = 0

    for p in pem:
        bayar11 += p.dibayar1
    
    bayar22 = 0

    for q in utang:
        bayar22 += q.dibayar
    
    bayar33 = 0

    for r in pem1:
        bayar33 += r.dibayar

    kas_keluar3 = (bayar11 + bayar22 + bayar33) + ((bayar11 + bayar22 + bayar33) * 75 / 100)

    jumlah1 = kas_masuk1 + kas_masuk2 + kas_masuk3 + kas_masuk4
    jumlah2 = kas_keluar1 + kas_keluar2 + kas_keluar3

    total = jumlah1 - jumlah2

    saldo_awal1 = models.SaldoAwal.objects.all()

    saldo_awal1 = models.SaldoAwal.objects.filter(usaha=id)

       
    return render(req, 'wia/wia75.html', {
    'id': id,
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
    })

def wia100(req, id):
    pen = models.penjualan1m.objects.all()
    pen2 = models.pend_lainm.objects.all()

    pen = models.penjualan1m.objects.filter(usaha=id)
    pen2 = models.pend_lainm.objects.filter(usaha=id)

    kas_masuk1 = 0
    for q in pen:
      kas_masuk1 += q.kas_masuk1() + (q.kas_masuk1() * 100 / 100)

    kas_masuk2 = 0
    for q in pen2:
      kas_masuk2 += q.jum_pend() + (q.jum_pend() * 100 / 100)

    penjualan1 = models.penjualan1m.objects.all()
    penjualan2 = models.pend_lainm.objects.all()

    penjualan1 = models.penjualan1m.objects.filter(usaha=id)
    penjualan2 = models.pend_lainm.objects.filter(usaha=id)

    total_terima1 = 0   

    for p in penjualan1:
      total_terima1 += p.terima 

    total_terima2 = 0   

    for p in penjualan2:
      total_terima2 += p.terima

    kas_masuk3 = ((total_terima1 + total_terima2) * 100 / 100) + (total_terima1 + total_terima2)

    utang = models.utangm.objects.all()

    utang = models.utangm.objects.filter(usaha=id)

    kas_masuk4 = 0
    for i in utang:
      kas_masuk4 += i.jum_utang() + (i.jum_utang() * 100 / 100)

    pem = models.pem_tunaim.objects.all()
    pem1 = models.pem_kreditm.objects.all()

    pem = models.pem_tunaim.objects.filter(usaha=id)
    pem1 = models.pem_kreditm.objects.filter(usaha=id)

    kas_keluar1 = 0
    for i in pem:
      kas_keluar1 += i.kas_keluar1() + (i.kas_keluar1() * 100 / 100)

    kas_keluar2 = 0
    for i in pem1:
      kas_keluar2 += i.kas_keluar2() + (i.kas_keluar2() * 100 / 100)

    utang = models.utangm.objects.all()
    pem = models.pem_kreditm.objects.all()
    pem1 = models.pem_tunaim.objects.all()

    utang = models.utangm.objects.filter(usaha=id)
    pem = models.pem_kreditm.objects.filter(usaha=id)
    pem1 = models.pem_tunaim.objects.filter(usaha=id)

    bayar11 = 0

    for p in pem:
        bayar11 += p.dibayar1
    
    bayar22 = 0

    for q in utang:
        bayar22 += q.dibayar
    
    bayar33 = 0

    for r in pem1:
        bayar33 += r.dibayar

    kas_keluar3 = (bayar11 + bayar22 + bayar33) + ((bayar11 + bayar22 + bayar33) * 100 / 100)

    jumlah1 = kas_masuk1 + kas_masuk2 + kas_masuk3 + kas_masuk4
    jumlah2 = kas_keluar1 + kas_keluar2 + kas_keluar3

    total = jumlah1 - jumlah2

    saldo_awal1 = models.SaldoAwal.objects.all()

    saldo_awal1 = models.SaldoAwal.objects.filter(usaha=id)

       
    return render(req, 'wia/wia100.html', {
    'id': id,
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
    })

#lrk
def lrk(req, id):
    usaha = models.usaha.objects.filter(pk=id).first()
    saldo_awal = models.SaldoAwal.objects.all()
    sawal = 0
    for q in saldo_awal:
      sawal += q.sawal()
    print(sawal)

    pen = models.penjualan1m.objects.all()
    pen2 = models.pend_lainm.objects.all()


    kas_masuk1 = 0
    for q in pen:
      kas_masuk1 += q.kas_masuk1()

    kas_masuk2 = 0
    for q in pen2:
      kas_masuk2 += q.jum_pend()

    penjualan1 = models.penjualan1m.objects.all()
    penjualan2 = models.pend_lainm.objects.all()


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


    kas_keluar1 = 0
    for i in pem:
      kas_keluar1 += i.kas_keluar1()

    kas_keluar2 = 0
    for i in pem1:
      kas_keluar2 += i.kas_keluar2()

    utang = models.utangm.objects.all()
    pem = models.pem_kreditm.objects.all()
    pem1 = models.pem_tunaim.objects.all()


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

    saldo = sawal + total
       
    return render(req, 'keperluan/lrk.html', {
    'id': id,
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
    'sawal': sawal,
    'saldo': saldo,
    })


