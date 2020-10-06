from django.contrib import admin
from django.urls import path, include 
from maghal.views import home 


urlpatterns = [
	path('admin/', admin.site.urls),	
	path('', include('maghal.urls'),
]
