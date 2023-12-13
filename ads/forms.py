from django import forms
from .models import Ads

class AdsForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = [
            'image', 'title', 'description', 'price',
            'contact', 'address', 'category', 'whatsapp',
            'telegram', 'instagram'
        ]
        