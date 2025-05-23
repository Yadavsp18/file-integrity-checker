from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    hash = models.CharField(max_length=64)
    uploaded_at = models.DateTimeField(auto_now_add=True)
