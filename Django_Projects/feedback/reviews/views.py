from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import date
from django.views import View

from .forms import ReviewForm

today_year = date.today().year

# Create your views here.

class ReviewView(View): 
    def get(self, request):
        form = ReviewForm()
        
        return render(request, 'reviews/index.html',{
            'form': form,
            'year': today_year
        })

    def post(self, request):
        form =  ReviewForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('thank-you')
        
        return render(request, 'reviews/index.html',{
            'year': today_year,
            'form': form
        })
    
class ThankYouPageView(View):
    def get(self, request):
        return render(request, 'reviews/thank_you.html',{
            'year': today_year
        })
