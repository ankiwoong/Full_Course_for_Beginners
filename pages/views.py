from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):         # *args, **kwargs
    # print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})
    # return HttpResponse("<h1>Hello World</h1>")         # string of HTML code


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})


def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})
