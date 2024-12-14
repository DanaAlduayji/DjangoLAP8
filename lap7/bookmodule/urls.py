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
]
