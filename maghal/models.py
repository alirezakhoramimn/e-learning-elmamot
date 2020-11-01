from django.db import models

from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.



PRO_CHOICES = (
		('Autoencoders', 'Deep Belief Net'),
		('Deep Belief Net','Deep Belief Net'),
		('Convolutional Neural Networks','Convolutional Neural Networks'),
		('Recurrent Neural Networks','Recurrent Neural Networks'),
		('Reinforcement Learning','Reinforcement Learning'),
		('Natural language processing','Natural language processing'),
		('Recommendation systems++','Recommendation systems'),
		('Bioinformatics','Bioinformatics'),
		('Mobile advertising', 'Mobile advertising'),
		('Financial fraud detection', 'Financial fraud detection'),
)

class Post(models.Model):
    name = models.CharField(max_length=100, choices=PRO_CHOICES,default='Autoencoders')

    title = models.CharField(max_length=100,default='')

    summary = models.CharField(max_length=300,blank=True,null=True,default='')

    body = RichTextUploadingField()
   # body = models.TextField()

    links = models.URLField(blank=True,null=True)

    def get_absolute_url(self):

        return reverse("detail", args =[self.name,self.number])
