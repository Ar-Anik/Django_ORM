from django.urls import path
from .views import Std_List, Thr_List, Employer_List, Book_List, Book_ISBN

urlpatterns = [
    path('', Std_List, name="studentlist"),
    path('teacherlist/', Thr_List, name='teacherlist'),
    path('employerlist/', Employer_List, name='employerlist'),
    path('booklist/', Book_List, name='booklist'),
    path('bookisbn/', Book_ISBN, name='bookisbn'),
]