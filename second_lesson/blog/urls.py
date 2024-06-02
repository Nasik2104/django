from django.urls import path

from blog import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about')
]
