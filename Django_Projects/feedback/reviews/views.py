from typing import Any
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponseRedirect
from datetime import date
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .models import Review

from .forms import ReviewForm

today_year = date.today().year

# Create your views here.


class ReviewView(CreateView):
    template_name = "reviews/index.html"
    model = Review
    success_url = "/thank-you"
    form_class = ReviewForm

    # get_context_data(self, **kwargs)

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    # def get(self, request):
    #     form = ReviewForm()

    #     return render(request, "reviews/index.html", {"form": form, "year": today_year})

    # def post(self, request):
    #     form = ReviewForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("thank-you")

    #     return render(request, "reviews/index.html", {"year": today_year, "form": form})


class ThankYouPageView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["year"] = today_year
        context["message"] = "Thank you for your valuable feedback"
        return context


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "review_list"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gte=3)
    #     return data


class ReviewDetailsView(DetailView):
    template_name = "reviews/review_details.html"
    model = Review

    # def get_context_data(self, **kwargs):
    #     requested_details = Review.objects.get(pk=kwargs["id"])
    #     context = super().get_context_data(**kwargs)
    #     context["year"] = today_year
    #     context["review"] = requested_details
    #     return context
