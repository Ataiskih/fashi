from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from product.views import (index, blog, blog_details, check_out,
    contact, faq, login, main, product, register, shop,
    shopping_cart)


urlpatterns = [
    path("", index, name="index"),
    path("blog/", blog, name="blog"),
    path("blog_details/", blog_details, name="blog_details"),
    path("check_out/", check_out, name="check_out"),
    path("contacts/", contact, name="contact"),
    path("faq/", faq, name="faq"),
    path("logins/", login, name="logins"),
    path("8/", main, name="main"),
    path("9/", product, name="product"),
    path("register/", register, name="register"),
    path("shop/", shop, name="shop"),
    path("shopping_cart/", shopping_cart, name="shopping_cart"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
