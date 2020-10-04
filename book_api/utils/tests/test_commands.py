import os
import pytest

from django.conf import settings

from book_api.books.management.commands.loadbooksdata import Command as LoadBooksData
from book_api.books.models import Book
from book_api.reviews.management.commands.loadreviewsdata import (
    Command as LoadReviewsData
)
from book_api.reviews.models import Review
from book_api.users.management.commands.loadusersdata import Command as LoadUserData
from book_api.users.models import User
from book_api.utils.testutils import get_csv_records


@pytest.mark.django_db
class TestCommands:

    def test_loadusersdata(self):
        """Test class handling `loadusersdata` management command."""

        # Given the management command and .csv with users
        load_users = LoadUserData()

        # When calling the handle() method and checking the results
        load_users.handle()
        users_queryset = User.objects.all()

        # Then assert all users have been added
        assert users_queryset.count() == get_csv_records(filename="assets/users.csv")

    def test_loadbooksdata(self):
        """Test class handling `loadbooksdata` management command."""

        # Given the management commands and .csv with books
        load_users = LoadUserData()
        load_books = LoadBooksData()

        # When calling the handle() method and checking the results
        load_users.handle()
        load_books.handle()
        books_queryset = Book.objects.all()

        # Then assert all users have been added
        assert books_queryset.count() == get_csv_records(filename="assets/books.csv")

    def test_loadreviewsdata(self):
        """Test class handling `loadreviewsdata` management command."""

        # Given the management commands and .csv with reviews
        load_users = LoadUserData()
        load_books = LoadBooksData()
        load_reviews = LoadReviewsData()

        # When calling the handle() method and checking the results
        load_users.handle()
        load_books.handle()
        load_reviews.handle()
        reviews_queryset = Review.objects.all()

        # Then assert all users have been added
        assert reviews_queryset.count() == get_csv_records(filename="assets/reviews.csv")
