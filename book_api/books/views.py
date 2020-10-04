from django.db.models import Avg
from django.http import HttpResponse
from django.views import View

from book_api.books.forms import BookForm
from book_api.books.models import Book
from book_api.reviews.models import Review
from book_api.reviews.views import REVIEW_FIELDS
from book_api.utils.responses import get_method_not_allowed_response
from book_api.utils.views import BaseAPIABCView, ModelFormView


class BookReviewsMixin:

    def _get_related_reviews(self):

        filtering = {}
        reviews_data = []

        book_pk = self.kwargs.get("pk", None)
        search_phrase = self.kwargs.get("search_phrase", None)

        if book_pk is not None:
            filtering.update({"book__pk": book_pk})
        if search_phrase is not None:
            filtering.update({"book__title__icontains": search_phrase})

        reviews_queryset = Review.objects.filter(**filtering).values(
            *REVIEW_FIELDS
        )
        for review in reviews_queryset:
            reviews_data.append(
                self._build_instance_data_dict(fields=REVIEW_FIELDS, instance=review)
            )

        return reviews_data


class SearchBooksView(BaseAPIABCView, BookReviewsMixin, View):

    model = Book
    queryset_fields = [
        "id", "user__name", "title", "description", "rating", "genre", "isbn"
    ]
    queryset_annotate = {"rating": Avg("reviews__rating")}
    additional_data = {"reviews": "_get_related_reviews"}

    def get(self, request, *args, **kwargs):

        self.queryset_filtering.update(
            {"title__icontains": self.kwargs.get("search_phrase")}
        )
        return HttpResponse(
            content_type="application/json",
            content=self.generate_json_response(),
            status=200
        )

    def post(self, request, *args, **kwargs):
        return get_method_not_allowed_response("POST")


class ListBooksView(BaseAPIABCView, View):

    model = Book
    queryset_fields = [
        "id", "user__name", "title", "description", "rating", "genre", "isbn"
    ]
    queryset_annotate = {"rating": Avg("reviews__rating")}

    def get(self, request, *args, **kwargs):

        return HttpResponse(
            content_type="application/json",
            content=self.generate_json_response(),
            status=200
        )

    def post(self, request, *args, **kwargs):
        return get_method_not_allowed_response("POST")


class BookDetailsView(BaseAPIABCView, BookReviewsMixin, View):

    model = Book
    queryset_fields = [
        "id", "user__name", "title", "description", "rating", "genre", "isbn"
    ]
    queryset_annotate = {"rating": Avg("reviews__rating")}
    additional_data = {"reviews": "_get_related_reviews"}

    def get(self, request, *args, **kwargs):

        self.queryset_filtering.update({"pk": self.kwargs.get("pk")})
        return HttpResponse(
            content_type="application/json",
            content=self.generate_json_response(),
            status=200
        )

    def post(self, request, *args, **kwargs):
        return get_method_not_allowed_response("POST")


class CreateBookView(View, ModelFormView):
    form = BookForm
