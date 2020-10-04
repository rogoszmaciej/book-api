from csv import reader
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from book_api.books.models import Book
from book_api.users.models import User


class LoadDataCommandMixin(BaseCommand):
    """
    Generic Mixin to support loading data from defined .csv files
    """

    file = None
    instance_class = None
    count = 0

    def _print_create_instance_success_message(self, instance):
        self.stdout.write(self.style.SUCCESS(
            f"Successfully created {instance.__class__.__name__} with pk {instance.pk}"
        ))

    def _print_success_message(self, instance):
        self.stdout.write(self.style.SUCCESS(
            f"Successfully loaded {self.count} {instance.__class__.__name__}s"
        ))

    @classmethod
    def _get_file_path(cls):
        return os.path.join(
            os.path.join(settings.BASE_DIR, "assets"), cls.file
        )

    @classmethod
    def _get_file_content(cls):
        with open(cls._get_file_path(), newline="") as csv_file:
            data = list(reader(csv_file))
            return data

    def _update_instance_data(self, header, row_item):
        if header == "user":
            row_item = User.objects.filter(name__iexact=row_item).first()
        if header == "isbn" and self.instance_class.__name__ != "Book":
            header = "book"
            row_item = Book.objects.filter(isbn__iexact=row_item).first()
        return {header: row_item}

    def load_object_from_row(self, headers, row_data):
        """
        Method saving object in database from row data;

        Need to be overloaded

        """

        instance_data = {}
        for header, row_item in zip(headers, row_data):
            instance_data.update(
                self._update_instance_data(header=header, row_item=row_item)
            )
        return self.instance_class.objects.create(**instance_data)

    def create_data_from_file(self):
        """
        Load data from set file
        """

        data = self._get_file_content()
        headers = data[0][0].split(";")[:-1]
        data = data[1:]

        for row_data in data:
            row_data = row_data[0].split(";")[0:-1]
            instance = self.load_object_from_row(
                headers=headers, row_data=row_data
            )
            self._print_create_instance_success_message(instance=instance)
            self.count += 1
        self._print_success_message(instance=instance)
