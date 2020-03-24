from django import forms
from .models import FavDetails


class FavsForm(forms.ModelForm):
    class Meta:
        model = FavDetails
        fields = "__all__"
