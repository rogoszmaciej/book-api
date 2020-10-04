from django.core import serializers
from django.http import HttpResponse
from django.views import View

from book_api.reviews.models import Review
from book_api.utils.responses import get_method_not_allowed_response
from book_api.utils.views import BaseAPIABCView


REVIEW_FIELDS = ["id", "book", "rating", "content", "created"]


class CreateReviewView(View):

    def get(self, request, *args, **kwargs):
        return get_method_not_allowed_response("GET")

    def post(self, request, *args, **kwargs):
        pass


class BookReviewsListView(BaseAPIABCView, View):

    model = Review
    queryset_fields = REVIEW_FIELDS

    def get(self, request, *args, **kwargs):
        self.queryset_filtering.update({"book__pk": self.kwargs.get("book_pk")})
        return HttpResponse(
            content_type="application/json",
            content=self.generate_json_response(),
            status=200
        )

    def post(self, request, *args, **kwargs):
        return get_method_not_allowed_response("POST")


class ReviewDetailsView(BaseAPIABCView, View):

    model = Review
    queryset_fields = REVIEW_FIELDS

    def get(self, request, *args, **kwargs):
        self.queryset_filtering.update({"pk": self.kwargs.get("pk")})
        return HttpResponse(
            content_type="application/json",
            content=self.generate_json_response(),
            status=200
        )

    def post(self, request, *args, **kwargs):
        return get_method_not_allowed_response("POST")
