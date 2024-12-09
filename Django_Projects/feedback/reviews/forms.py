from django import forms 
from .models import Review

# class ReviewForms(forms.Form):
#     username = forms.CharField(label="Your Name", max_length=100, error_messages={
#         'max_length': "The name entered to too long. Please write a short name",
#         'required': "You cannot leave the name field black!"
#     })


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__" # ['field_1', 'field_2']
        # exclude = ['owner_comment'] 
        labels = {
            'username': 'Your Name',
            'review_text': 'Your Feedback',
            'rating': 'Your Rating'
        }
        error_messages = {
            'username': {
            'required': "The name entered to too long. Please write a short name",
            'max_length':'You cannot leave the name field black!',
            },
            'rating': {
                'min_value': "Please enter a valid rating between 1 and 5.",
                'max_value': "Please enter a valid rating between 1 and 5.",
            }
        }
        