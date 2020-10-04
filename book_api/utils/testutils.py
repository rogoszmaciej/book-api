import os

from django.conf import settings

from book_api.books.management.commands.loadbooksdata import Command as LoadBooksData
from book_api.reviews.management.commands.loadreviewsdata import (
    Command as LoadReviewsData
)
from book_api.users.management.commands.loadusersdata import Command as LoadUserData


def get_csv_records(filename):
    """
    Returns numbers of file lines - 1 (First line is header).
    Result is number of records
    """

    filename = os.path.join(settings.BASE_DIR, filename)

    with open(filename) as file:
        records = sum(1 for line in file) - 1
    return records


def load_test_data():
    """
    Load data from csv files for tests
    """

    load_users = LoadUserData()
    load_books = LoadBooksData()
    load_reviews = LoadReviewsData()

    # When calling the handle() method and checking the results
    load_users.handle()
    load_books.handle()
    load_reviews.handle()
