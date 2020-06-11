from django.shortcuts import render
from django.views import View

# BASE_VIEW Class = VIEW
class CourseView(View):
    template_name = "about.html"

    def get(self, request, *args, **kwargs):
        # GET method
        return render(request, self.template_name, {})  # new_obj = CourseView()

    # def post(request, *args, **kwargs):
    #     return render(request, "about.html", {})


# HTTP METHODS
def my_fbv(request, *args, **kwargs):
    return render(request, "about.html", {})
