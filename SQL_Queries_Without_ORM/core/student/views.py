from django.shortcuts import render
from django.db import connection
from django.db.models import Q
from .models import Student, Teacher


# Create your views here.

# Sometimes even Manager.raw() isn’t quite enough: you might need to 
# perform queries that don’t map cleanly to models, 
# or directly execute UPDATE, INSERT, or DELETE queries.

# In these cases, you can always access the database directly, 
# routing around the model layer entirely.

# The object django.db.connection represents the default 
# database connection. To use the database connection, 
# call connection.cursor() to get a cursor object. 
# Then, call cursor.execute(sql, [params]) to execute 
# the SQL and cursor.fetchone() or cursor.fetchall() 
# to return the resulting rows.

# django.db.connection ----> database connection represent
# connection.cursor -----> create object
# cursor.execute("sql query") ----> execute sql query
# cursor.fetchone() or cursor.fecthall()

def list(request):
    cursor = connection.cursor()
    cursor.execute("SELECT count(*) FROM student_student")
    data = cursor.fetchone()

    print(data)
    print(connection.queries)

    context = {
        'data': data,
    }

    return render(request, 'output.html', context)

def alllist(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM student_student")
    data = cursor.fetchall()

    print(data)
    print(connection.queries)

    context = {
        'data': data,
    }

    return render(request, 'output1.html', context)


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def dictionary(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM student_student")
    data = dictfetchall(cursor)

    print(data)
    print(connection.queries)

    context = {
        'data': data,
    }

    return render(request, 'output1.html', context)
