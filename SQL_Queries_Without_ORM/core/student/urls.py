from django.urls import path
from .views import dictionary, list, alllist

urlpatterns = [
    path('', list, name='name'),
    path('alllist/', alllist, name='alllist'),
    path('dictionary/', dictionary, name='dictionary'),
]
