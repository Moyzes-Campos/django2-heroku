from django.urls import path
from .views import index, blog, contato, posts


urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('blog', blog, name='blog'),
    path('blog/<int:pk>', posts, name='posts'),
]