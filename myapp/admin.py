from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.mail import send_mail
from django.conf import settings  # Import settings to access DEFAULT_FROM_EMAIL
from .models import (
    Book,
    ContactQuery,
    CustomUser,
    Forum,
    ForumComment,
    ForumLike,
    Payment,
)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "condition",
        "genre",
        "used_duration",
        "sale_amount",
        "rent_amount",
        "status",
        "user",
        "for_sale",
        "for_rent",
    ]
    search_fields = ["title", "author"]
    list_filter = ["condition", "genre", "status"]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if "status" in form.changed_data:
            self.send_status_email(obj)

    def send_status_email(self, book):
        subject = "Book Request Status Update"
        message = f"Dear {book.user.first_name},\n\n"
        if book.status == "approved":
            message += f'Your request to {"sell" if book.for_sale else "rent"} the book "{book.title}" has been approved.'
        elif book.status == "rejected":
            message += f'Your request to {"sell" if book.for_sale else "rent"} the book "{book.title}" has been rejected.'
        message += "\n\nThank you,\nNegative Zero"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [book.user.email])


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
        "favorite_book_genre",
        "mobile_number",
    ]
    search_fields = ["username", "email"]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "status", "created_at")
    readonly_fields = ("user", "book", "created_at")

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if "status" in form.changed_data:
            self.send_status_email(obj)

    def send_status_email(self, payment):
        subject = "Payment Status Update"
        message = f"Dear {payment.user.first_name},\n\n"
        if payment.status == "approved":
            message += f'Your payment for the book "{payment.book.title}" has been approved. We will contact you shortly for delivery details.'
        elif payment.status == "rejected":
            message += f'Your payment for the book "{payment.book.title}" has been rejected. Please contact us for more information.'
        message += "\n\nThank you,\nNegative Zero"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [payment.user.email])


@admin.register(ContactQuery)
class ContactQueryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject")


@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "genre", "created_at", "user"]
    search_fields = ["title", "author", "genre"]
    list_filter = ["genre", "created_at"]


@admin.register(ForumComment)
class ForumCommentAdmin(admin.ModelAdmin):
    list_display = ["forum", "user", "comment", "created_at"]
    search_fields = ["comment"]
    list_filter = ["created_at"]


@admin.register(ForumLike)
class ForumLikeAdmin(admin.ModelAdmin):
    list_display = ["forum", "user", "created_at"]
    list_filter = ["created_at"]
