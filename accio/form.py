from django import forms
from django.utils.translation import gettext_lazy as _

from accio.models import Cartridge, Compound, next_compound_code


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

    # def __init__(self, *args, **kwargs):
    #     super(CompoundForm, self).__init__(*args, **kwargs)
    #     if self.initial.get('code') is None:
    #         self.initial['code'] = next_compound_code
    #     self.fields['code'].widget.attrs['readonly'] = True
    #     self.fields['code'].help_text = _('auto-generated non-editable')

    pass
