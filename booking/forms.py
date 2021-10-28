from django import forms
from .models import Guest, Stay

class GuestCreateForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('honorific', 'first', 'last', 'vip', 'email')

class GuestUpdateForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('honorific', 'first', 'last', 'vip', 'email')

class StayCreateForm(forms.ModelForm):
    class Meta:
        model = Stay
        fields = ('roomid','guestid','empid','start','end')
