from django.urls import path

from .views import my_fbv, CourseView

app_name = "courses"

urlpatterns = [
    path("", CourseView.as_view(template_name="contact.html"), name="courses-list"),
    # path("", my_fbv, name="courses-list"),
]
