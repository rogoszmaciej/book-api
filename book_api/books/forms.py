from django.forms import ModelForm

from book_api.books.models import Book


class BookForm(ModelForm):

    class Meta:
        model = Book
        fields = ["user", "title", "description", "isbn"]
