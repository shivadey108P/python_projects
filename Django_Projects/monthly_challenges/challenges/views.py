from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
challenges = {
    'january': "Maintain proper diet and eat healthy food only, no Junk!",
    'february': "Do workouts on daily basis!",
    'march': "Complete Django course, study 1 section per day!",
    'april': "Walk 10k steps daily",
    'may': "Get a new python-full stalk web developer job",
    'june': "Start preparing for AWS Developer certification course!",
    'july': "Read 3 Canto in Bhavgwat-Gita daily.",
    'august': 'Complete python DSA course',
    'september': 'Start calisthenics training',
    'october': 'Start the python data analytics course',
    'november': 'Complete AWS Developer certification',
    'december': 'Save money and renovate your house.'
}

def index(request):
    months = list(challenges.keys())
    list_items = ""
    
    for month in months:
        month_path = reverse('month_challenge', args=[month])
        list_items += f"<li> <a href='{month_path}'> {month.capitalize()} </a> </li><br>"
    
    response_data = f"<ul> {list_items} </ul>"
    return HttpResponse(response_data)

def monthly_challenges_by_number(request, month):
    months = list(challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound('<h1>404 - response not found!</h1><br> <p>Invalid Month!</p>')
    
    forward_month = months[month-1]
    redirect_url = reverse('month_challenge', args=[forward_month])
    return HttpResponseRedirect(redirect_url)

def monthly_challenges(request, month):
    global challenges
    try:
        new_challenge = f"{challenges[month.lower()]}"
        return render(request, 'challenges/challenge.html', {
            "text": new_challenge
        })
    except KeyError:
        return HttpResponseNotFound('<h1>404 - response not found!</h1><br> <p>Entered month is not correct! Please check for spellings.</p>')