from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import SetPasswordForm

from django.contrib.auth import get_user_model

from .models import Chat

class ChatCreateForm(ModelForm):
    class Meta:
        model = Chat
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    body = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            'autofocus': True,
            "placeholder":"投稿を入力してください",
        }),
        help_text="節度を守って登校してください",
        error_messages={
            "required" : "投稿を入力してください",
        },
    )

