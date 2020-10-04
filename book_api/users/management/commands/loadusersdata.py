from book_api.users.models import User
from book_api.utils.commands import LoadDataCommandMixin


class Command(LoadDataCommandMixin):
    """
    Command to load users(authors) from assets/users.csv
    """

    file = "users.csv"
    help = "Load users from file"
    instance_class = User

    def handle(self, *args, **options):
        self.create_data_from_file()
