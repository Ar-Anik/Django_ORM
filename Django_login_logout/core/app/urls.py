from django.urls import path, include
from .views import registrationform, studentform, studentlist

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('registration/', registrationform, name='registration'),

    path('studentcreate/', studentform, name='studentcreate'),

    path('studentlist/', studentlist, name='studentlist'),
]
