from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin
from myapp import views
from django.views.static import serve
from django.urls import re_path
from django.contrib.auth.views import LogoutView
from django.conf.urls import handler404
from myapp.views import custom_404  # Replace 'your_app' with the actual app name

handler404 = 'myapp.views.custom_404'

urlpatterns = [
    path("", views.login_view, name="login"),
    path("signup/", views.signup, name="signup"),
    path(
        "home_sell_donate_rent/",
        views.home_sell_donate_rent,
        name="home_sell_donate_rent",
    ),
    path("home_buy_rent/", views.home_buy_rent, name="home_buy_rent"),
    path("donate-book/", views.donate_book, name="donate_book"),
    path("buy_books/", views.buy_books, name="buy_books"),
    path(
        "rent_books_available/", views.rent_books_available, name="rent_books_available"
    ),
    path("book/<int:pk>/", views.book_detail, name="book_detail"),
    path("rent_book/<int:pk>/", views.book_detail, name="rent_book_detail"),
    path("sell-book/", views.sell_book, name="sell_book"),
    path("rent-book/", views.rent_book, name="rent_book"),
    path("rent_books/", views.rent_books_available, name="rent_books_available"),
    path("payment/<int:pk>/<str:mode>/", views.payment, name="payment"),
    path("payment/success/", views.payment_success, name="payment_success"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("profile/", views.profile, name="profile"),  # Add profile URL
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("contact/", views.contact, name="contact"),
    path("contact/success/", views.contact_success, name="contact_success"),
    path("about_us/", views.about_us, name="about_us"),  # Add about us URL
    path(
        "forums/", views.forum_list, name="forum_list"
    ),  # Make sure to use views.forum_list
    path("forums/<int:pk>/", views.forum_detail, name="forum_detail"),
    path("forums/create/", views.forum_create, name="forum_create"),
    path("forums/<int:pk>/like/", views.forum_like, name="forum_like"),
    path("forums/<int:pk>/delete/", views.forum_delete, name="forum_delete"),
    path(
        "forums/<int:pk>/comment/", views.forum_comment, name="forum_comment"
    ),  # Add this line for comments
    path("datecv/", views.datecv, name="datecv"),
    path("calendar/", views.calendar, name="calendar"),
    path("weather/", views.weather, name="weather"),
    path("cvgenerator/", views.cvgenerator, name="cvgenerator"),
    path("home/", views.home, name="home"),
    re_path(r'^ms86568092\.txt$', serve, {
        'document_root': settings.BASE_DIR,
        'path': 'ms86568092.txt',
    }),
    # path("", views.portfolio, name="portfolio"),
    # path('trigger404/', views.trigger_404, name='trigger_404'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)