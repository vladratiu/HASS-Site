from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('homepage', views.home, name= 'homepage'),
    path('exec', views.exec, name = 'exec'),
    path('partner', views.partner, name = 'partner'),
    path('events', views.events, name = 'events'),
    path('contact', views.contact, name = 'contact'),
    
]