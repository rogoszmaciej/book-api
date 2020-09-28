from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser):
    """
    Book API User model

    Requires username and email, Other fields are optional.
    """

    username = models.CharField(
        _("Username"),
        max_length=255,
        unique=True,
        help_text=_("User's account username."),
        error_messages={"unique": _("A user with that username already exists.")},
    )
    email = models.EmailField(_("Email address"), blank=True, unique=True)
    created_on = models.DateTimeField(_("Date joined"), auto_now_add=True)
    is_staff = models.BooleanField(
        verbose_name=_("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        verbose_name=_("Active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        ordering = ["id"]
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email
