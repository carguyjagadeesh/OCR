from django import forms
from .models import UploadImage

class UploadImageForm(forms.ModelForm):
    
    class Meta:
        model = UploadImage
        fields = ['image']

class TranslationForm(forms.Form):
    text_to_translate = forms.CharField(label='Text to Translate', widget=forms.TextInput)

class Sentiment(forms.Form):
    text_to_translate = forms.CharField(label='Enter Your Text Here', widget=forms.TextInput)    