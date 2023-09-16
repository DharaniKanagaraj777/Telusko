from django.urls import path

from . import views


 
urlpatterns=[
    path('',views.home,name='sub'),
    path('add',views.add,name='div')
]