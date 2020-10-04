from django.contrib import admin

from book_api.reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ["id", "book", "rating"]
    list_filter = ["book"]
