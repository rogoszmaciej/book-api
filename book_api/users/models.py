from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    """
    Book API User model

    Requires username and email, Other fields are optional.
    """

    username = models.CharField(
        verbose_name=_("Username"),
        max_length=255,
        unique=True,
        help_text=_("User's account username."),
        error_messages={"unique": _("A user with that username already exists.")},
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=255,
        help_text=_("User's name."),
    )
    email = models.EmailField(verbose_name=_("Email address"), blank=True, unique=True)
    created_on = models.DateTimeField(verbose_name=_("Date joined"), auto_now_add=True)
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
