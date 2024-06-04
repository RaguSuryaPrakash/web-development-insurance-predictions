from django import forms
from .models import *


class insuForm(forms.ModelForm):
    class Meta():
        model=insuModel
        fields=['age','bmi','children','sex_male','smoker_yes']
