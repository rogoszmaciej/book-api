from django.db import models
from django.utils.translation import gettext_lazy as _

from book_api.users.models import User


class Book(models.Model):

    user = models.ForeignKey(
        User, verbose_name=_("Book Author"), on_delete=models.CASCADE
    )
    title = models.CharField(verbose_name=_("Book Title"), max_length=255)
    description = models.CharField(verbose_name=_("Book Description"), max_length=255)
    genre = models.CharField(verbose_name=_("Genre"), max_length=255)
    isbn = models.CharField(verbose_name=_("ISBN"), unique=True, max_length=20)

    class Meta:
        ordering = ["id"]
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def __str__(self):
        return self.title
