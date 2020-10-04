from abc import ABC
from datetime import datetime
import json

from django.http import HttpResponse

from book_api.utils.responses import get_method_not_allowed_response


class ModelFormView:

    form = None
    success_message = "Successfully created!"

    def get(self, request, *args, **kwargs):
        return get_method_not_allowed_response("GET")

    def post(self, request, *args, **kwargs):

        form_instance = self.form(request.data)
        if form_instance.is_valid():
            form_instance.save()
            return HttpResponse(
                {"success": self.success_message},
                status=200
            )
        return HttpResponse(
            form_instance.errors.as_data(),
            status=400
        )


class BaseAPIABCView(ABC):
    """
    Abstract View class to enable fast implementation of API views
    """

    model = None
    queryset_fields = []
    queryset_annotate = {}
    queryset_filtering = {}
    queryset_ordering = ["id"]
    additional_data = {}

    def __init__(self):
        error = "{} view class is missing model attribute declaration".format(
            self.__class__.__name__
        )
        assert self.model is not None, error

    @classmethod
    def get_queryset(cls):

        return cls.model.objects.filter(**cls.queryset_filtering).annotate(
            **cls.queryset_annotate).values(*cls.queryset_fields).order_by(
            *cls.queryset_ordering
        )

    @staticmethod
    def _build_instance_data_dict(fields, instance):

        instance_data = {}
        for field in fields:
            if isinstance(instance[field], datetime):
                instance[field] = instance[field].strftime("%d.%m.%Y")
            instance_data.update({field: instance[field]})

        return instance_data

    def _generate_instance_data(self, instance):
        instance_data = self._build_instance_data_dict(
            fields=self.queryset_fields, instance=instance
        )
        if self.additional_data:
            for key, item in self.additional_data.items():
                if hasattr(self, item):
                    instance_data.update({key: getattr(self, item)()})

        return instance_data

    def generate_json_response(self):

        objects_list = []
        for instance in self.get_queryset():
            objects_list.append(self._generate_instance_data(instance=instance))

        return json.dumps(objects_list, ensure_ascii=False)
