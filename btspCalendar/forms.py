
from django import forms


class ChangeDateNext(forms.Form):
    year=forms.CharField(max_length=50)
    month=forms.CharField(max_length=50)

