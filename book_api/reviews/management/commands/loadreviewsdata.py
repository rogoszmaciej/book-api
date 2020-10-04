from book_api.reviews.models import Review
from book_api.utils.commands import LoadDataCommandMixin


class Command(LoadDataCommandMixin):
    """
    Command to load reviews from assets/reviews.csv
    """

    file = "reviews.csv"
    help = "Load reviews from file"
    instance_class = Review

    def handle(self, *args, **options):
        self.create_data_from_file()
