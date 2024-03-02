from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'name')

        # Add the functionality to automatically update the fields in the form at a later stage
        '''
        exclude_fields = set('is_staff', 'is_superuser', 'last_login', 'date_joined', 'groups', 'user_permissions')
        fields = [f.name for f in User._meta.fields if f.name not in exclude_fields]
        '''





