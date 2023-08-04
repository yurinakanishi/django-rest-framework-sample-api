from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError


class Command(createsuperuser.Command):
    help = "Create a superuser with a password non-interactively"

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            "--password",
            dest="password",
            default=None,
            help="Specifies the password for the superuser.",
        )

    def handle(self, *args, **options):
        options.setdefault("interactive", False)
        name = options.get("name")
        email = options.get("email")
        password = options.get("password")
        database = options.get("database")

        if not (name and email and password):
            raise CommandError("--name, --email and --password are required options")

        user_data = {
            "name": name,
            "email": email,
            "password": password,
        }

        exists = (
            self.UserModel._default_manager.db_manager(database)
            .filter(name=name)
            .exists()
        )
        if not exists:
            self.UserModel._default_manager.db_manager(database).create_superuser(
                **user_data
            )
