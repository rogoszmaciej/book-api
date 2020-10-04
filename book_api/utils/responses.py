from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _


def get_method_not_allowed_response(method):
    return HttpResponse((_("%s method not allowed") % method), status=405)
