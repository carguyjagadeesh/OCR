from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name='upload_image'),
    path('translate/', views.translation_view, name='translate'),
    path('Positive/',views.sentimentAnalysics,name='sentiment'),
]