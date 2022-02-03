from django.urls import path
from .views import Not_Q_object, Q_object, or_query, student_list

urlpatterns = [
    path('', student_list),

    path('orquery/', or_query, name='orquery'),

    path('qobject/', Q_object, name='qobject'),

    path('notqobject/', Not_Q_object, name='notqobject'),
]
