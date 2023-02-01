from django import forms
from .models import Comment, Profile, Order
from django.contrib.auth.models import User


class OrderCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("order", "user", "text")
        widgets = {"order": forms.HiddenInput(), "user": forms.HiddenInput()}


class UserUpdateForm(forms.ModelForm):
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nuotrauka']

class MyDateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

class OrderCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['terminas', 'automobilis', 'status']
        # widgets = {"terminas": forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'})}
        widgets = {"terminas": MyDateTimeInput()}