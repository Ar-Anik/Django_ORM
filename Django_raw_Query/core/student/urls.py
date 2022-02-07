from unicodedata import name
from django.urls import path
from .views import limiting_query, list, variable, where, loop

urlpatterns = [
    path('', list, name='list'),
    path('where/', where, name='where'),
    path('loop/', loop, name='loop'),
    path('variable/', variable, name='variable'),
    path('limit/', limiting_query, name='limit'),
]