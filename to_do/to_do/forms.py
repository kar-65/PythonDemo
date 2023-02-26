
from django import forms

from to_doApp.models import dolist


class doform(forms.ModelForm):
    class Meta:
        model= dolist
        fields=['name','prior','date']
