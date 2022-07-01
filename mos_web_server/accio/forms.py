from django import forms
from django.utils.translation import gettext_lazy as _

from mos_web_server.accio.models import Cartridge, Compound, next_compound_code, QuantMethod, next_quant_method_code


# Create your forms here.
class CartridgeForm(forms.ModelForm):
    class Meta:
        model = Cartridge
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CartridgeForm, self).__init__(*args, **kwargs)

    pass


class CompoundForm(forms.ModelForm):
    class Meta:
        model = Compound
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CompoundForm, self).__init__(*args, **kwargs)
        if self.initial.get('code') is None:
            self.initial['code'] = next_compound_code
        self.fields['code'].widget.attrs['readonly'] = True
        self.fields['code'].help_text = _('auto-generated non-editable')

    pass


class QuantMethodForm(forms.ModelForm):
    class Meta:
        model = QuantMethod
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(QuantMethodForm, self).__init__(*args, **kwargs)
        if self.initial.get('code') is None:
            self.initial['code'] = next_quant_method_code
        self.fields['code'].widget.attrs['readonly'] = True
        self.fields['code'].help_text = _('auto-generated non-editable')

    pass
