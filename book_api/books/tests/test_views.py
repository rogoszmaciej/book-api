import pytest

from django.urls import reverse_lazy
from django.test.client import Client

from book_api.utils.testutils import get_csv_records, load_test_data


@pytest.mark.django_db
class TestBookViews:

    def test_search_books_view(self):

        # Given the data from .csv files and a test Client
        load_test_data()
        client = Client()

        # When calling API endpoint with search phrase
        url = reverse_lazy('books:search', kwargs={"search_phrase": "głębi"})
        response = client.get(url)
        response_content = response.json()
        reviews = response_content[0].get("reviews")

        # Then assert there's a result and only one item returned
        assert response.status_code, 200
        assert len(response.json()) == 1
        assert len(reviews) == 5

    def test_list_books_view(self):

        # Given the data from .csv files and a test Client
        load_test_data()
        client = Client()

        # When calling API endpoint with search phrase
        url = reverse_lazy('books:list')
        response = client.get(url)
        response_content = response

        # Then assert all books are returned
        assert response.status_code == 200
        print(response_content.content)
        assert len(response_content) == get_csv_records(filename="assets/books.csv")
