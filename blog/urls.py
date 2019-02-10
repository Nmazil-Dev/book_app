from django.urls import path
from . import views
from .views import MyBooksListView, BookUpdateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.get_name, name='form'),
    path('form/search/', views.search, name='search'),
    path('form/search/no_results/', views.no_results, name='no_results'),
    path('book/<int:pk>/', views.book_details, name='book_details'),
    path('my_books/', login_required(MyBooksListView.as_view()), name='my_books'),
    path('my_books/book/<int:pk>/', views.my_book_details, name='my_book_details'),
    path('my_books/book/edit/<int:pk>/', BookUpdateView.as_view(), name ='edit_book'),
]
