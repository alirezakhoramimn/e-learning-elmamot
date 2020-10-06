from django.urls import path
from .views import update_view, MaghalListView,create_view,maghal_detail

app_name = 'maghal'
urlpatterns = [
    path('', MaghalListView.as_view(), name='home'),
    path('detail/<str:name>/<int:number>',maghal_detail, name='detail'), 
    path('create/', create_view, name='create'),
    path('detail/<str:name>/<int:number>/update', update_view, name = 'update'),
]
