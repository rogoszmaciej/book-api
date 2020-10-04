from book_api.books.models import Book
from book_api.utils.commands import LoadDataCommandMixin


class Command(LoadDataCommandMixin):
    """
    Command to load books from assets/books.csv
    """

    file = "books.csv"
    help = "Load books from file"
    instance_class = Book

    def handle(self, *args, **options):
        self.create_data_from_file()
