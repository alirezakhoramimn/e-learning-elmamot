from django.urls import path
from .views import update_view, MaghalListView,MaghalCreateView,maghal_detail

app_name = 'maghal'
urlpatterns = [
    path('', MaghalListView.as_view(), name='home'),
    path('detail/<str:name>/<int:number>',maghal_detail, name='detail'), 
    path('create/', MaghalCreateView.as_view(), name='create'),
    path('update/<str:name>/<int:number>', update_view, name = 'update'),
]
