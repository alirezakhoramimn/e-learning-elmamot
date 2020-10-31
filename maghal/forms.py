from django import forms
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget


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
