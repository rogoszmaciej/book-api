from book_api.reviews.models import Review


def get_books_by_reviews():

    books_dict = {}
    book_id = 0

    for review in Review.objects.all().values(
        "rating", "content", "book__id", "book__user__name", "book__title",
        "book__description", "book__isbn"
    ):
        review_data = {"rating": review["rating"], "content": review["content"]}
        book_data = {
            "author": review["book__user__name"], "title": review["book__title"],
            "description": review["book__description"], "isbn": review["book__isbn"],
            "reviews": []
        }

        if book_id > 0:
            if review["book__id"] != book_id:
                book_id = review["book__id"]
            if book_id not in books_dict:
                books_dict[book_id].update(book_data)

        books_dict[book_id]["reviews"].append(review_data)

        return books_dict
