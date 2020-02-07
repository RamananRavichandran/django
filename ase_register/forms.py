from django import forms
from .models import Ase


class AseForm(forms.ModelForm):

    class Meta:
        model = Ase
        fields = ('fullname','emp_code','mobile','dateoj')
        labels = {
            'fullname':'Full Name',
            'emp_code':'Employee Code',
            'mobile':'Mobile Number',
            'dateoj':'Date of Join'
        }