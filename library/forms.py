from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import User, Reader, Genre

class WriterSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_writer = True
        if commit:
            user.save()
        return user

class ReaderSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    town = forms.CharField(max_length=60)

    my_favorite_book_genre = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "town", "password1", "password2")

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_reader = True
        user.save()
        reader = Reader.objects.create(user=user)
        reader.my_favorite_book_genre.add(*self.cleaned_data.get('my_favorite_book_genre'))
        return user

class My_Favorite_Book_Genre_Form(forms.ModelForm):
    my_favorite_book_genre = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    class Meta:
        model = Reader
        fields = ('my_favorite_book_genre', )
        widgets = {
            'my_favorite_book_genre': forms.CheckboxSelectMultiple
        }

