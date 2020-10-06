from django import forms 
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget

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
 
class MaghalCreateForm(forms.ModelForm):

	number = forms.IntegerField()
		
	name = forms.ChoiceField(choices=PRO_CHOICES,widget=forms.Select(attrs={'class':'form-control '}))
	


	title =forms.CharField(required=True,max_length=100,widget=forms.TextInput(  
		attrs={
			'class': 'form-control ',
			'placeholder': 'تایتل',
			'id': 'hi',
		}))

	summary = forms.CharField(required=False,max_length=150,widget=forms.Textarea(
		attrs={
			'class':"form-control ",
			'placeholder': 'لطفا یک خلاصه ای از این مقاله بزار در حد ۱۵ - 20 کلمه '
		}
	))

	links = forms.URLField(required=False,widget=forms.URLInput(
		attrs = {
			'class': 'form-control '
		}
	))

	body = forms.CharField(label='man babatam ',required=True,widget=CKEditorUploadingWidget())


	class Meta:
		model = Post
		fields ='__all__'

