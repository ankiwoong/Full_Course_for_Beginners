from django.urls import path

from .views import (
    # my_fbv,
    CourseView,
    CourseListView,
)

app_name = "courses"

urlpatterns = [
    path("", CourseListView.as_view(), name="courses-list"),
    # path("", my_fbv, name="courses-list"),
    path("<int:id>/", CourseView.as_view(), name="courses-detail"),
]
