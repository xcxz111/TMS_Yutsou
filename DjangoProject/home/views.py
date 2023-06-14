from django.shortcuts import render, redirect
from django.contrib import messages
from home.forms import FeedbackForm

# Create your views here.

carousel = [
    {"master": "Diana", "work": "Storytelling", "job": "Business", "video": "images/works/video-1.MOV"},
    {"master": "Olga", "work": "Creative", "job": "Design", "video": "images/works/video-2.MOV"},
    {"master": "Diana", "work": "Modeling", "job": "Fashion", "video": "images/works/video-3.MOV"},
    {"master": "Diana", "work": "Acting", "video": "images/works/video-4.MOV"},
    {"master": "Olga", "work": "Influencer", "video": "images/works/video-5.MOV"},
    {"master": "Diana", "work": "Education", "video": "images/works/video-6.MOV"},
    {"master": "Olga", "work": "Education", "video": "images/works/video-6.MOV"}
]

students = [
    {"name": "Candice", "work": "Storytelling", "job": "Business", "img": "images/students/student-1.jpeg"},
    {"name": "William", "work": "Creative", "job": "Design", "img": "images/students/student-2.jpeg"},
    {"name": "Taylor", "work": "Modeling", "job": "Fashion", "img": "images/students/student-3.jpeg"},
    {"name": "Nick", "work": "Acting", "img": "images/students/student-4.jpeg"}
]


def home_page(request):
    return render(request, "home.html", {"carousel": carousel, "carousel_students": students, "page_tag": "home"})


def about(request):
    return render(request, "about.html", {"page_name": "About Pod", "page_tag": "about"})


def studio(request):
    return render(request, "studio.html", {"page_tag": "studio"})


def masters(request):
    return render(request, "masters.html", {"page_tag": "masters"})


def contact(request):
    fform = FeedbackForm()
    if request.method == "POST":
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            fform.save()
            messages.info(request, "Ваше сообщение отправлено")
            return redirect("contact_page")
    return render(request, "contact.html", {"fform": fform, "page_tag": "contact"})



