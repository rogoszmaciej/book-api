from django.contrib import admin
from django.db.models import Avg

from book_api.books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ["id", "user", "title", "isbn", "rating"]
    list_filter = ["user"]

    def rating(self, instance):
        average = instance.books.aggregate(average=Avg("rating")).get("average", 0)
        return "{0:.1f}".format(average)
