from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _

from .models import User


class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=150,
                                 required=True,
                                 label=_("First name"))
    last_name = forms.CharField(max_length=150,
                                required=True,
                                label=_("Last name"))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name',
                  'last_name',
                  'username',
                  'password1',
                  'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['username'].validators = []

    def clean_username(self):
        username = self.cleaned_data['username']
        if self.instance and self.instance.username == username:
            return username
        return super().clean_username()
