from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from book_api.books.models import Book


review_rating_validator = RegexValidator(
    regex=r"^([1-5]{1})$",
    message="Must be an integer value between 1 and 5 inclusive."
)


class Review(models.Model):

    book = models.ForeignKey(
        Book, verbose_name=_("Book"), on_delete=models.CASCADE, related_name="reviews"
    )
    rating = models.IntegerField(
        verbose_name=_("Book Rating"), validators=[review_rating_validator], default=0
    )
    content = models.CharField(verbose_name=_("Rating Content"), max_length=255)
    created = models.DateTimeField(
        verbose_name=_("Date & Time Created"), auto_now_add=True,
    )

    class Meta:
        ordering = ["id"]
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")

    def __str__(self):
        return f"{self.id}. {self.book} - {self.rating}"
