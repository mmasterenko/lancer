from .models import CustomUser
from django.apps import apps as django_apps
from django.core.exceptions import ImproperlyConfigured


class CustomBackend(object):
    def authenticate(self, car_number=None, password=None, **kwargs):
        UserModel = self.get_user_model()
        if car_number is None:
            car_number = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            user = UserModel._default_manager.get_by_natural_key(car_number)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            UserModel().set_password(password)

    def get_user_model(self):
        """
        Returns the User model that is active in this project.
        """
        try:
            return django_apps.get_model('clientArea.CustomUser')
        except ValueError:
            raise ImproperlyConfigured("AUTH_USER_MODEL must be of the form 'app_label.model_name'")
        except LookupError:
            raise ImproperlyConfigured(
                "AUTH_USER_MODEL refers to model '%s' that has not been installed" % settings.AUTH_USER_MODEL
            )

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
