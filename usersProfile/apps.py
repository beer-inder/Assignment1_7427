from django.apps import AppConfig


class UsersprofileConfig(AppConfig):
    name = 'usersProfile'

    def ready(self):
        import usersProfile.signals
