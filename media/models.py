from django.db import models

class MediaFile(models.Model):
    file = models.FileField(upload_to='media/')
    
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or str(self.file)
    
class Media(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/images/') 
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title