from django.urls import path, re_path

from book_api.reviews.views import (
    CreateReviewView, BookReviewsListView, ReviewDetailsView
)


app_name = "reviews"


urlpatterns = [
    path("create/", CreateReviewView.as_view(), name="create"),
    re_path(
        r"^details/(?P<pk>\d+)/$",
        ReviewDetailsView.as_view(), name="details"
    ),
    re_path(
        r"^book_reviews/(?P<book_pk>\d+)/$",
        BookReviewsListView.as_view(),
        name="book_reviews"
    ),
]
