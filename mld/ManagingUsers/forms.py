from django.contrib.auth.forms import UserCreationForm
from .models import MLDUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = MLDUser
        fields  = ('username', 'password1', 'password2', 'email')
