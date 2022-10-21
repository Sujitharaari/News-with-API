from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index.html'),
    path('contact',views.contact,name='contact.html'),
    path('category',views.category,name='category.html'),
    path('single',views.single,name='single.html')

]