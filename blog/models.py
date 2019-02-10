from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.



class Result(models.Model):
    title = models.TextField()
    author = models.TextField()
    images = models.TextField()
    page_count = models.TextField()

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    images = models.TextField()
    page_count = models.IntegerField()
    current_page = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    def percent_complete(self):
        if self.page_count == 0:
            return ('0%')
        percent =  self.current_page / self.page_count
        percent *= 100
        return str(round(percent)) + '%'

    def get_absolute_url(self):
        return reverse('my_book_details', args=[str(self.id)])
