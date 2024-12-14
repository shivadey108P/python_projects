from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import UserProfile


# Create your views here.
class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["user_name"].label = "Your Name"
        form.fields["user_email"].label = "Your Email"
        form.fields["user_image"].label = "Your Image"
        return form


class ProfileView(ListView):
    template_name = "profiles/profile.html"
    model = UserProfile
    context_object_name = "profiles"
