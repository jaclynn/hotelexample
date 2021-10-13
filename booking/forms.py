from django import forms
from .models import Guest

class GuestCreateForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('honorific', 'first', 'last', 'vip', 'email')

class GuestUpdateForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('honorific', 'first', 'last', 'vip', 'email')
