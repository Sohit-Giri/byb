from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings

from myapp.models import Book, Forum, ForumComment, ForumLike
from .forms import (
    ContactForm,
    CustomUserCreationForm,
    BookForm,
    DonateBookForm,
    EditProfileForm,
    ForumCommentForm,
    ForumForm,
    PaymentForm,
    RentBookForm,
)
import logging

logger = logging.getLogger(__name__)


def signup(request):
    if request.method == "POST":
        logger.debug("Signup form submitted.")
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            logger.debug("Signup form is valid.")
            user = form.save()
            login(request, user)
            # Send confirmation email
            subject = "Welcome to Negative Zero"
            message = f"Dear {user.first_name},\n\nThank you for joining Negative Zero. We are excited to have you on board.\n\nBest regards,\nNegative Zero Team"
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
            return redirect("home_buy_rent")
        else:
            logger.debug("Signup form is not valid: %s", form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, "signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home_buy_rent")
        else:
            return render(
                request, "login.html", {"form": form, "error": "Invalid credentials"}
            )
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def home_sell_donate_rent(request):
    return render(request, "home_sell_donate_rent.html")

def datecv(request):
    return render(request, "datecv.html")

def calendar(request):
    return render(request, "calendar.html")

def weather(request):
    return render(request, "weather.html")

def cvgenerator(request):
    return render(request, "cvgenerator.html")

def home(request):
    return render(request, "home.html")


def home_buy_rent(request):
    user = request.user
    books_for_buying = Book.objects.filter(for_sale=True)[:6]
    books_for_renting = Book.objects.filter(for_rent=True)[:6]
    books_based_on_preference = Book.objects.filter(genre=user.favorite_book_genre)[:6]
    recent_forums = Forum.objects.order_by("-created_at")[
        :5
    ]  # Fetch recent forum posts

    context = {
        "books_for_buying": books_for_buying,
        "books_for_renting": books_for_renting,
        "books_based_on_preference": books_based_on_preference,
        "recent_forums": recent_forums,  # Pass to the template
    }
    return render(request, "home_buy_rent.html", context)


@login_required
def donate_book(request):
    if request.method == "POST":
        form = DonateBookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.status = "pending"
            book.save()
            return render(
                request,
                "donate_book.html",
                {
                    "message": "You will be notified via email within 24 hours if your book donation is approved by admin.",
                    "form": DonateBookForm(),
                },
            )
        else:
            return render(request, "donate_book.html", {"form": form})
    else:
        form = DonateBookForm()
    return render(request, "donate_book.html", {"form": form})


@login_required
def sell_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user  # Ensure this is a CustomUser instance
            book.status = "pending"
            book.save()
            logger.debug("Book saved successfully")
            return render(
                request,
                "sell_book.html",
                {
                    "message": "You will be notified via email within 24 hours if your book sale is approved by admin.",
                    "form": BookForm(),
                },
            )
        else:
            logger.debug("Form errors: %s", form.errors)
    else:
        form = BookForm()
    return render(request, "sell_book.html", {"form": form})


@login_required
def rent_book(request):
    if request.method == "POST":
        form = RentBookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.status = "pending"
            book.save()
            return render(
                request,
                "rent_book.html",
                {
                    "message": "You will be notified via email within 24 hours if your book rental is approved by admin.",
                    "form": RentBookForm(),
                },
            )
        else:
            return render(request, "rent_book.html", {"form": form})
    else:
        form = RentBookForm()
    return render(request, "rent_book.html", {"form": form})


def buy_books(request):
    search_query = request.GET.get("search", "")
    genre_filter = request.GET.get("genre", "")
    author_filter = request.GET.get("author", "")
    sort_order = request.GET.get("sort", "")

    books = Book.objects.filter(for_sale=True)

    if search_query:
        books = books.filter(
            Q(title__icontains=search_query)
            | Q(author__icontains=search_query)
            | Q(genre__icontains=search_query)
        )
    if genre_filter:
        books = books.filter(genre=genre_filter)
    if author_filter:
        books = books.filter(author=author_filter)
    if sort_order == "price_low_to_high":
        books = books.order_by("sale_amount")
    elif sort_order == "price_high_to_low":
        books = books.order_by("-sale_amount")

    genres = Book.objects.values_list("genre", flat=True).distinct()
    authors = Book.objects.values_list("author", flat=True).distinct()

    return render(
        request,
        "buy_books.html",
        {"books": books, "genres": genres, "authors": authors},
    )


def rent_books_available(request):
    search_query = request.GET.get("search", "")
    genre_filter = request.GET.get("genre", "")
    author_filter = request.GET.get("author", "")
    sort_order = request.GET.get("sort", "")

    books = Book.objects.filter(for_rent=True)

    if search_query:
        books = books.filter(
            Q(title__icontains=search_query)
            | Q(author__icontains=search_query)
            | Q(genre__icontains=search_query)
        )
    if genre_filter:
        books = books.filter(genre=genre_filter)
    if author_filter:
        books = books.filter(author=author_filter)
    if sort_order == "price_low_to_high":
        books = books.order_by("rent_amount")
    elif sort_order == "price_high_to_low":
        books = books.order_by("-rent_amount")

    genres = Book.objects.values_list("genre", flat=True).distinct()
    authors = Book.objects.values_list("author", flat=True).distinct()

    return render(
        request,
        "rent_books_available.html",
        {"books": books, "genres": genres, "authors": authors},
    )


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "book_detail.html", {"book": book})


@login_required
def payment(request, pk, mode):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.book = book
            return redirect("payment_success")
    else:
        form = PaymentForm()
    context = {
        "book": book,
        "form": form,
        "mode": mode,
    }
    return render(request, "payment.html", context)


def payment_success(request):
    return render(request, "payment_success.html")


@login_required
def profile(request):
    user = request.user
    context = {
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "favorite_book_genre": user.favorite_book_genre,
        "mobile_number": user.mobile_number,
        "profile_picture": user.profile_picture.url if user.profile_picture else None,
    }
    return render(request, "profile.html", context)


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, "edit_profile.html", {"form": form})


# Add this view for the about us page
def about_us(request):
    logger.debug("About Us page accessed.")
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_success")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})


def contact_success(request):
    return render(request, "contact_success.html")


# Forums


def forum_list(request):
    forums = Forum.objects.all()
    return render(request, "forums/forum_list.html", {"forums": forums})


def forum_detail(request, pk):
    forum = get_object_or_404(Forum, pk=pk)
    comments = ForumComment.objects.filter(forum=forum)
    user_has_liked = ForumLike.objects.filter(forum=forum, user=request.user).exists()
    likes = ForumLike.objects.filter(forum=forum)
    context = {
        "forum": forum,
        "comments": comments,
        "form": ForumCommentForm(),
        "user_has_liked": user_has_liked,
        "likes": likes,
    }
    return render(request, "forums/forum_detail.html", context)


@login_required
def forum_create(request):
    if request.method == "POST":
        form = ForumForm(request.POST, request.FILES)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.user = request.user
            forum.save()
            return redirect("forum_list")
    else:
        form = ForumForm()
    return render(request, "forums/forum_form.html", {"form": form})


@login_required
def forum_like(request, pk):
    forum = get_object_or_404(Forum, pk=pk)
    like, created = ForumLike.objects.get_or_create(forum=forum, user=request.user)
    if not created:
        like.delete()
    return redirect("forum_detail", pk=pk)


@login_required
def forum_comment(request, pk):
    forum = get_object_or_404(Forum, pk=pk)
    if request.method == "POST":
        form = ForumCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.forum = forum
            comment.user = request.user
            comment.save()
    return redirect("forum_detail", pk=pk)


@login_required
def forum_delete(request, pk):
    forum = get_object_or_404(Forum, pk=pk)
    if request.user == forum.user or request.user.is_staff:
        forum.delete()
    return redirect("forum_list")
