from os import name
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('category/<int:id>', category, name='category'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('blog_details/', blog_details, name='blog_details'),
    path('contact/', contact, name='contact'),
    path('elements/', elements, name='elements'),
    path('login/', login, name='login'),
    path('sign-up/', sign_up, name='sign-up'),
    path('main/', my_Main, name='main'),
    path('feedback/', feedback, name='feedback'),
    path('search/', search, name='search'),
    path('post-details/<int:id>', post_details, name='post-details'),
]
