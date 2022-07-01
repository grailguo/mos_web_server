from django import forms

from mos_web_server.reparo.models import Device


# Create your forms here.
class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)

    pass
