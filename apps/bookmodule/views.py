from django.shortcuts import render

# Create your views here.
from django.db.models import Q, Sum, Avg, Max, Min, Count

from django.http import HttpResponse
from .models import Book, Student, Address

# def index(request):
#     name = request.GET.get("name") or "world!"
#     return render(request, "bookmodule/index.html", {"name": name})

# New index2 view with a parameter in the URL path
def index2(request, val1=0):
    # val1 is an integer parameter passed through the URL
    return HttpResponse(f"value1 = {val1}")


def viewbook(request, bookId):
    # Assume these books are in your database or a static list for now
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    
    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    elif book2['id'] == bookId:
        targetBook = book2

    # Create the context with the target book details
    context = {'book': targetBook}
    
    # Render the show.html template and pass the context
    return render(request, 'bookmodule/show.html', context)

def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html',)

def view_one_book(request, bookId):
    return render(request, 'bookmodule/one_book.html', {'bookId': bookId})


def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def search_books(request):
    books = __getBooksList()
    newBooks = []

    if request.method == 'POST':
        keyword = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')  # Checkbox for title
        isAuthor = request.POST.get('option2')  # Checkbox for author

        for item in books:
            contained = False
            if isTitle and keyword in item['title'].lower():
                contained = True
            if not contained and isAuthor and keyword in item['author'].lower():
                contained = True
            if contained:
                newBooks.append(item)

        # Redirect to bookList.html with the filtered books
        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    # If not POST, just show the form
    return render(request, 'bookmodule/search_books.html')


# List of books (static data)
def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]



def simple_query(request):
    mybook = Book(title='Continuous Delivery', author='J. Humble and D. Farley', price=97.00, edition=1)
    mybook.save()  # Save the object to the database

    mybooks = Book.objects.filter(title__icontains='Delivery')  # Filter books where title contains 'and'
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


def lookup_query(request):
    mybooks = Book.objects.filter(author__isnull=False) \
                          .filter(title__icontains='Delivery') \
                          .filter(edition__gte=1) \
                          .exclude(price__gte=100)[:10]
                          
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')  # Fallback page if no books match


def task1(request):
    books = Book.objects.filter(Q(price__lte=50))
    return render(request,"bookmodule/lap8/task1.html", {'books': books})

def task2(request):
    books = Book.objects.filter(edition__gt=2, title__icontains='qu') | Book.objects.filter(edition__gt=2, author__icontains='qu')
    return render(request, 'bookmodule/lap8/task2.html', {'books': books})

def task3(request):
    books = Book.objects.filter(
        Q(edition__lte=2) & ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, "bookmodule/lap8/task3.html", {'books': books})

# views.py
def task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, "bookmodule/lap8/task4.html", {'books': books})


def task5(request):
    aggregation = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, "bookmodule/lap8/task5.html", {'aggregation': aggregation})


def task7(request):
    city_counts = Address.objects.annotate(num_students=Count('student'))
    return render(request, "bookmodule/lap8/task7.html", {'city_counts': city_counts})
