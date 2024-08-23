from django import forms
from .models import Soildata

class DataForm(forms.ModelForm):
    class Meta:
        model = Soildata
        fields = ["ec", "ph", "type"]
