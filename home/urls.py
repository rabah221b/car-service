from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('about/',views.about, name='about'),
    path('booking/',views.booking, name='booking'),
    path('vechiles/',views.vechile, name='vechiles'),
    path('contact/',views.contact, name='contact'),
    path('classofvechile/',views.classofvechile, name='classofvechile'),
     
]
