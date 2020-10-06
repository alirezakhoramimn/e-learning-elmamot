from django.db import models

from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


	
PRO_CHOICES = (
		('HTML5', 'HTML'),
		('Bootstrap4','Bootstrap4'),
		('Css3','Css3'),
		('Js','js'),
		('Kotlin','Kotlin'),
		('Java','java'),
		('C++','C++'),
		('Perl','Perl'),
		('C-Sharp', 'C-Sharp'),
		('Python', 'Python'),
		('GraphQL', 'GraphQL'),
		('REST', 'REST'),
		('PostgreSQL', 'PostgreSQL'),
		('MySQL', 'MySQL'),
		('SQLServer','SQLServer'),
		('linux', 'linux'),
		('git','git'),
		('docker', 'docker'), 
)
 
class Post(models.Model):
    name = models.CharField(max_length=100, choices=PRO_CHOICES,default='HTML')
	 

    number = models.PositiveIntegerField(verbose_name='iin chandomie?',default=1)


    title = models.CharField(max_length=100,default='')

    summary = models.CharField(max_length=300,blank=True,null=True,default='')

    body = RichTextUploadingField()

    links = models.URLField(blank=True,null=True)

    def get_absolute_url(self):

        return reverse("detail", args =[self.name,self.number])
	
