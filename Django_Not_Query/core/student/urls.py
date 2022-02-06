from django.urls import path
from .views import list, list_gte, list_lte, qnot

urlpatterns = [
    path('', list, name='list'),
    path('listgte/', list_gte, name='listgte'),
    path('listlte/', list_lte, name='listlte'),
    path('qnot/', qnot, name='qnot'),
]
