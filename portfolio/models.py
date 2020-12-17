from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/') # 업로드된 이미지들을 images 폴더안에 넣으라
    image_thumbnail = ImageSpecField(source='image', 
        processors=[ResizeToFill(120, 80)], format='JPEG')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title
