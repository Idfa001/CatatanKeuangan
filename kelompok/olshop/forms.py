from django.forms import ModelForm
from bootstrap_datepicker_plus import DatePickerInput
from . import models

 
class penjualan1f(ModelForm):
    class Meta:
        model = models.penjualan1m
        exclude = [ 'saldo_awal', 'terima' , 'owner' ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(penjualan1f, self).__init__(*args, **kwargs)
        self.fields['barang'].queryset = models.barangm.objects.filter(owner=user)

class saldoawalf(ModelForm):
    class Meta:
        model = models.saldoawalm
        exclude = [ 'owner' ] 


class utangf(ModelForm):
    class Meta:
        model = models.utangm
        exclude = ['dibayar', 'owner']
        widgets = {
            'jatuh_tempo': DatePickerInput(format='%d-%m-%Y'),
        }

class pend_lainf(ModelForm):
    class Meta:
        model = models.pend_lainm
        exclude = [ 'terima', 'owner' ]

class pem_tunaif(ModelForm):
    class Meta:
        model = models.pem_tunaim
        exclude = [ 'dibayar', 'owner' ]

class pem_kreditf(ModelForm):
    class Meta:
        model = models.pem_kreditm
        exclude = [ 'dibayar1', 'owner' ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(pem_kreditf, self).__init__(*args, **kwargs)
        self.fields['barang'].queryset = models.barangm.objects.filter(owner=user)


class barangf(ModelForm):
    class Meta:
        model = models.barangm
        exclude = ['owner']

