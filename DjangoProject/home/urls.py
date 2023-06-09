from django.urls import path
from home.views import home_page, about, contact, studio, masters


urlpatterns = [
    path("", home_page, name="home_page"),
    path("about/", about, name="about_page"),
    path("contact/", contact, name="contact_page"),
    path("studio/", studio, name="studio_page"),
    path("masters/",masters, name="masters_page")

]