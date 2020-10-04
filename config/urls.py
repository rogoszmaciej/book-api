from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("books/", include("book_api.books.urls", namespace="books")),
    path("reviews/", include("book_api.reviews.urls", namespace="reviews"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
