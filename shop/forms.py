from django import forms

from shop.models import ColorModel


class ColorModelAdminForms(forms.ModelForm):
    code = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))

    class Meta:
        model = ColorModel
        fields = '__all__'
