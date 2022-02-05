from django.urls import path
from .views import list, allvalue, values

urlpatterns = [
    path('', list, name='list'),
    path('allvalue/', allvalue, name='allvalue'),
    path('values/', values, name='values'),
]