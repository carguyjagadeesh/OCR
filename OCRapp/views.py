from django.shortcuts import render, redirect
from django.conf import settings
from .pytesseract import image_to_string
from PIL import Image
from django.http import HttpRequest
from os import path
from .forms import UploadImageForm,TranslationForm,Sentiment
from googletrans import Translator, constants
from pprint import pprint
import re
from .utils import sentiment
def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()
            image_path = uploaded_image.image.path
            
            image = Image.open(image_path)
            text = image_to_string(image)
            print(text)
            return render(request, 'ocr_results.html', {'text': text})
    else:
        form = UploadImageForm()
    return render(request, 'upload_image.html', {'form': form})
def translation_view(request):
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            text_to_translate = form.cleaned_data['text_to_translate']
        
            translator = Translator()
            translation = translator.translate(text_to_translate,dest="en") 
            
            
            return render(request, 'lang_translate.html', {'translation': translation.text})
    else:
        form = TranslationForm()

    return render(request, 'Sentance_input.html', {'form': form})  
def sentimentAnalysics(request) :
    if request.method =='POST':
        form = Sentiment(request.POST)            
        if form.is_valid():
            form = form.cleaned_data['text_to_translate']
            sentiment1 = sentiment(form)
            return render(request, 'postiveSentiment.html', {'form': sentiment1}) 
    else:
        form = Sentiment()

    return render(request, 'Sentance_Taken.html', {'form': form})  
            
            
            
            
    
    
    
    