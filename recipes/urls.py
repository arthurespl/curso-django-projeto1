from django.urls import path

from recipes.views import home, sobre


urlpatterns = [
    path('', home, name='Home'),
    path('sobre/', sobre, name='Sobre'),
]
