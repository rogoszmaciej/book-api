from django.urls import path, re_path

from book_api.books.views import (
    CreateBookView, ListBooksView, BookDetailsView, SearchBooksView
)


app_name = "books"


urlpatterns = [
    path("create/", CreateBookView.as_view(), name="create"),
    path("list/", ListBooksView.as_view(), name="list"),
    re_path(r"^details/(?P<pk>\d+)/$", BookDetailsView.as_view(), name="details"),
    re_path(
        r"^search/(?P<search_phrase>\w+)/$",
        SearchBooksView.as_view(), name="search"
    )
]
