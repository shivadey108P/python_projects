from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view(), name="review-form"),
    path("thank-you", views.ThankYouPageView.as_view()),
    path("review", views.ReviewListView.as_view(), name="review-list"),
    path("review/<int:pk>", views.ReviewDetailsView.as_view(), name="review-detail"),
]
