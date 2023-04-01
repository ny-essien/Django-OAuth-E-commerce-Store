from django.urls import path
from . import views

app_name  = "e_commerce"

urlpatterns = [

    path("", views.homepage, name = "home"),

    path("signin/", views.signin, name = "signin"),

    path("signup/", views.signup, name = "signup"),

    path("logout/", views.logoutPage, name="logout-page"),
]