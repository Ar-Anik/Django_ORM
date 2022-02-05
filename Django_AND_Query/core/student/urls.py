from django.urls import path
from .views import list, qand

urlpatterns = [
   path('', list, name='list'),
   path('qand/', qand, name='qand'),
]
