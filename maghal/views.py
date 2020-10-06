
from .models import Post 
from .forms import MaghalCreateForm 
from django.views import generic 

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.shortcuts import redirect, render, reverse
#  your views here.

class MaghalCreateView(generic.edit.CreateView):
	form_class = MaghalCreateForm
	template_name = 'maghal/create.html'
	queryset = Post.objects.all()
	
	def form_valid(self, form):
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('detail',kwargs={'name':self.object.name, 'number':self.object.number})
 



def create_view(request): 
    form = MaghalCreateForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
        reverse('detail',kwargs={'name':form.name, 'number':form.number})

    context = {
        'form' :form,   
    
    }   
    return render(request, "maghal/create.html", context) 


def maghal_detail(request, name, number):
    post = get_object_or_404(Post, name=name , number=number)

    return render(request, 'maghal/detail.html', { "lang_post": post })





class MaghalListView(generic.ListView):
    model = Post
    context_object_name = 'langs'
    template_name = 'maghal/home.html'

# update view for details 
def update_view(request, id): 
    context ={} 
    obj = get_object_or_404(Post, name=name, number=number) 
    form = MaghalCreateForm(request.POST or None, instance = obj) 
    if form.is_valid(): 
        form.save() 
        reverse('detail',kwargs={'name':self.object.name, 'number':self.object.number})

    context["form"] = form 
  
    return render(request, "maghal/update.html.html", context) 




