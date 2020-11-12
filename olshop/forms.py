from django.forms import ModelForm
from bootstrap_datepicker_plus import DatePickerInput
from . import models




class usahaf(ModelForm):
    class Meta:
        model = models.usaha
        exclude =['owner']

class penjualan1f(ModelForm):
    class Meta:
        model = models.penjualan1m
        exclude = [ 'saldo_awal', 'terima' , 'usaha' ]
        widgets = {
            'jatuh_tempo': DatePickerInput(format='%d-%m-%Y'),
        }

    def __init__(self, *args, **kwargs):
        usaha = kwargs.pop('usaha', None)
        super(penjualan1f, self).__init__(*args, **kwargs)
        self.fields['barang'].queryset = models.barangm.objects.filter(usaha=usaha)

class saldoawalf(ModelForm):
    class Meta:
        model = models.saldoawalm
        exclude = [ 'usaha' ] 


class utangf(ModelForm):
    class Meta:
        model = models.utangm
        exclude = ['dibayar', 'usaha']
        widgets = {
            'jatuh_tempo': DatePickerInput(format='%d-%m-%Y'),
        }

class pend_lainf(ModelForm):
    class Meta:
        model = models.pend_lainm
        exclude = [ 'terima', 'usaha' ]
        widgets = {
            'jatuh_tempo': DatePickerInput(format='%d-%m-%Y'),
        }

class pem_tunaif(ModelForm):
    class Meta:
        model = models.pem_tunaim
        exclude = [ 'dibayar', 'usaha' ]
        widgets = {
            'jatuh_tempo': DatePickerInput(format='%d-%m-%Y'),
        }

class pem_kreditf(ModelForm):
    class Meta:
        model = models.pem_kreditm
        exclude = [ 'dibayar1', 'usaha' ]
        widgets = {
            'jatuh_tempo': DatePickerInput(format='%d-%m-%Y'),
        }

    def __init__(self, *args, **kwargs):
        usaha = kwargs.pop('usaha', None)
        super(pem_kreditf, self).__init__(*args, **kwargs)
        self.fields['barang'].queryset = models.barangm.objects.filter(usaha=usaha)


class barangf(ModelForm):
    class Meta:
        model = models.barangm
        exclude = ['usaha']

