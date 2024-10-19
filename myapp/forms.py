from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ContactQuery, CustomUser, Book, Forum, ForumComment, Payment


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "favorite_book_genre",
            "password1",
            "password2",
            "mobile_number",
            "profile_picture",
        ]


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "condition",
            "genre",
            "photo1",
            "photo2",
            "used_duration",
            "sale_amount",
            "rent_amount",
            "for_sale",
            "for_rent",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter book title"}),
            "author": forms.TextInput(attrs={"placeholder": "Enter author name"}),
            "condition": forms.Select(
                choices=[("new", "New"), ("second_hand", "Second Hand")]
            ),
            "genre": forms.Select(
                choices=[
                    ("fiction", "Fiction"),
                    ("nonfiction", "Non-Fiction"),
                    ("mystery", "Mystery"),
                    ("biography", "Biography"),
                    ("science", "Science"),
                    ("history", "History"),
                    ("fantasy", "Fantasy"),
                ]
            ),
            "used_duration": forms.TextInput(attrs={"placeholder": "e.g. 2 years"}),
            "sale_amount": forms.TextInput(attrs={"placeholder": "e.g. 500 NRs"}),
            "rent_amount": forms.TextInput(
                attrs={"placeholder": "Monthly rent e.g. 500 NRs"}
            ),
        }


class RentBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "condition",
            "genre",
            "photo1",
            "photo2",
            "used_duration",
            "rent_amount",
            "for_rent",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter book title"}),
            "author": forms.TextInput(attrs={"placeholder": "Enter author name"}),
            "condition": forms.Select(
                choices=[("new", "New"), ("second_hand", "Second Hand")]
            ),
            "genre": forms.Select(
                choices=[
                    ("fiction", "Fiction"),
                    ("nonfiction", "Non-Fiction"),
                    ("mystery", "Mystery"),
                    ("biography", "Biography"),
                    ("science", "Science"),
                    ("history", "History"),
                    ("fantasy", "Fantasy"),
                ]
            ),
            "used_duration": forms.TextInput(attrs={"placeholder": "e.g. 2 years"}),
            "rent_amount": forms.TextInput(
                attrs={"placeholder": "Monthly rent e.g. 500 NRs"}
            ),
        }


class DonateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "condition",
            "genre",
            "photo1",
            "photo2",
            "used_duration",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter book title"}),
            "author": forms.TextInput(attrs={"placeholder": "Enter author name"}),
            "condition": forms.Select(
                choices=[("new", "New"), ("second_hand", "Second Hand")]
            ),
            "genre": forms.Select(
                choices=[
                    ("fiction", "Fiction"),
                    ("nonfiction", "Non-Fiction"),
                    ("mystery", "Mystery"),
                    ("biography", "Biography"),
                    ("science", "Science"),
                    ("history", "History"),
                    ("fantasy", "Fantasy"),
                ]
            ),
            "used_duration": forms.TextInput(attrs={"placeholder": "e.g. 2 years"}),
        }

    def save(self, commit=True):
        book = super().save(commit=False)
        book.donation_request = True
        if commit:
            book.save()
        return book


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["payment_screenshot"]


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            "profile_picture",
            "email",
            "mobile_number",
            "favorite_book_genre",
            "first_name",
            "last_name",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "mobile_number": forms.TextInput(attrs={"placeholder": "Mobile Number"}),
            "favorite_book_genre": forms.TextInput(
                attrs={"placeholder": "Favorite Book Genre"}
            ),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactQuery
        fields = ["name", "email", "subject", "message"]


class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ["title", "author", "genre", "photo", "post"]


class ForumCommentForm(forms.ModelForm):
    class Meta:
        model = ForumComment
        fields = ["comment"]
