from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),  # maps to the index view
    # path('index2/<int:val1>/', views.index2),  # maps to the index2 view with an integer parameter
    # path('<int:bookId>/', views.viewbook),  # New URL pattern for book details
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.view_one_book, name='books.one_book'),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('search/', views.search_books, name='search_books'),
    path('simple/query', views.simple_query, name='simple_query'),
    path('complex/query', views.lookup_query, name='lookup_query'),
     # Task 1: Books with price <= 50 using Q operator
    path('lab8/task1', views.task1, name='task1'),

    # Task 2: Books with editions > 2 and title/author containing 'qu'
    path('lab8/task2', views.task2, name='task2'),

    # Task 3: Books with editions <= 2 and title/author not containing 'qu'
    path('lab8/task3', views.task3, name='task3'),

    # Task 4: Books ordered by title
    path('lab8/task4', views.task4, name='task4'),

    # Task 5: Aggregation functions (count, sum, avg, max, min)
    path('lab8/task5', views.task5, name='task5'),

    # Task 7: Show number of students in each city
    path('lab8/task7', views.task7, name='task7'),
]
