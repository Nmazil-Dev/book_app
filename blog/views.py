from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from .models import Result, Book
import requests
from .forms import NameForm, PageForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
import time
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    Result.objects.all().delete()
    return render(request, 'home.html')

def get_name(request):
    Result.objects.all().delete()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            data = form.cleaned_data.get("book_search")
            data = data.replace(' ', "+")
            return search(request, data)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

def search(request, data):
    search = data
    url = "https://www.googleapis.com/books/v1/volumes?q=" + search

    r = requests.get(url)
    content = r.json()
    try:
        data = content['items']
    except:
        return redirect('no_results')


    title = []
    images = []
    pages =[]
    author = []

    for book in data:
        new = (book['volumeInfo'])
        try:
            title.append(new['title'])
        except:
            title.append('N/A')
        try:
            pages.append(new['pageCount'])
        except:
            pages.append(0)
        try:
            book_author = ' '.join(new['authors'])
            author.append(book_author)
        except:
            author.append('N/A')
        try:
            image_url = (new['imageLinks'])
            image = (image_url['thumbnail'])
            images.append(image)
        except:
            images.append('N/A')

    book1 = []
    book2 = []
    book3 = []
    book4 = []
    book5 = []
    book6 = []
    book7 = []
    book8 = []
    book9 = []
    book10 = []

    x = 0
    while x < 10:
        if x == 0:
            book1.extend((title[x], author[x], images[x], pages[x]))
            x+=1
        elif x == 1:
            book2.extend((title[x], author[x], images[x], pages[x]))
            x+=1
        elif x == 2:
            book3.extend((title[x], author[x], images[x], pages[x]))
            x+=1
        elif x == 3:
            book4.extend((title[x], author[x], images[x], pages[x]))
            x+=1
        elif x == 4:
            book5.extend((title[x], author[x], images[x], pages[x]))
            x+=1
        elif x == 5:
            book6.extend((title[x], author[x], images[x], pages[x]))
            x+=1
        elif x == 6:
            book7.extend((title[x], author[x], images[x], pages[x]))
            x+=1
        elif x == 7:
            book8.extend((title[x], author[x], images[x], pages[x]))
            x+=1
        elif x == 8:
            book9.extend((title[x], author[x], images[x], pages[x]))
            x+=1
        elif x == 9:
            book10.extend((title[x], author[x], images[x], pages[x]))
            x+=1
        else:
            x+=1

    result1 = Result.objects.create(title=book1[0], author=book1[1], images=book1[2], page_count=book1[3])
    result2 = Result.objects.create(title=book2[0], author=book2[1], images=book2[2], page_count=book2[3])
    result3 = Result.objects.create(title=book3[0], author=book3[1], images=book3[2], page_count=book3[3])
    result4 = Result.objects.create(title=book4[0], author=book4[1], images=book4[2], page_count=book4[3])
    result5 = Result.objects.create(title=book5[0], author=book5[1], images=book5[2], page_count=book5[3])
    result6 = Result.objects.create(title=book6[0], author=book6[1], images=book6[2], page_count=book6[3])
    result7 = Result.objects.create(title=book7[0], author=book7[1], images=book7[2], page_count=book7[3])
    result8 = Result.objects.create(title=book8[0], author=book8[1], images=book8[2], page_count=book8[3])
    result9 = Result.objects.create(title=book9[0], author=book9[1], images=book9[2], page_count=book9[3])
    result10 = Result.objects.create(title=book10[0], author=book10[1], images=book10[2], page_count=book10[3])
    results_list = Result.objects.all()
    context = {'results_list': results_list}
    return render(request, 'search.html', context)

def no_results(request):
    return render(request, 'no_results.html')



def book_details(request, pk):
    if User.is_authenticated:
        current_user = request.user
    result = get_object_or_404(Result, pk=pk)
    context = {'result': result}
    if request.method == 'POST':
        new_book = Book.objects.create(title=result.title, author=result.author, images=result.images, page_count=result.page_count, owner=current_user)
        new_book.save()
        return redirect('my_books')

    return render(request, 'book_details.html', context)


class MyBooksListView(ListView):
    model = Book
    template_name = 'my_book_list.html'

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)

def my_book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = PageForm(request.POST, instance=book)

    if form.is_valid():
        if form.cleaned_data.get('current_page') <= book.page_count:
            form.save()
        else:
            return redirect('my_book_details', pk)

    context = {'book': book, 'form': form}

    if request.method == 'POST':
        if 'delete_book' in request.POST:
            book.delete()
            return redirect('my_books')


    return render(request, 'my_book_details.html', context)

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'edit_book.html'
    fields = ['title', 'author', 'page_count']
