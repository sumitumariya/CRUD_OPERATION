from django.urls import path
from .views import *

urlpatterns= [
     path('',home,name='home'),
     path('about/',about,name='about'),
     path('contact/',contact,name='contact'),
     path('register/',register,name='register'),
     path('expert/',expert,name='expert'),
     path('login/',login,name='login'),
     path('registerdata/',registerdata,name='registerdata'),
     path('logindata/',logindata,name='logindata'),
     path('Querydata/',Querydata,name='Querydata'),
     path('Show/',Show,name='Show'),
     path('delete/<int:pk>/<ml>',delete,name='delete'),
     path('editpage/<int:pk>',editpage,name='editpage'),
     path('update/<int:pk>',updatedata,name='update'),
]

