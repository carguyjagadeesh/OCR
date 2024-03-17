from django.db import models

class UploadImage(models.Model):
    image = models.ImageField(upload_to="image/")
    uploaded_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "OCRImages"
        
        
