from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('/product/<int:product_id>', views.product, name='product')
]
