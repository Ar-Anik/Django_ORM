from django.urls import path
from .views import cancel, list, manyfield, onefield, selector

urlpatterns = [
    path('', list, name='list'),
    path('selector/', selector, name='selector'),
    path('onefield/', onefield, name='onefield'),
    path('manyfield/', manyfield, name='manyfield'),
    path('cancel/', cancel, name='cancel'),
]
