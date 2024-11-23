from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
challenges = [
    "Maintain proper diet and eat healthy food only, no Junk!",
    "Do workouts on daily basis!",
    "Complete Django course, study 1 section per day!",
    "Walk 10k steps daily",
    "Get a new python-full stalk web developer job",
    "Start preparing for AWS Developer certification course!",
    "Read 3 Canto in Bhavgwat-Gita daily."
]

def monthly_challenges(request, month):
    global challenges
    new_challenge = None
    if month.lower() == 'january':
        new_challenge = challenges[0]
    elif month.lower() == 'february':
        new_challenge = challenges[1]
    elif month.lower() == 'march':
        new_challenge = challenges[2]
    elif month.lower() == 'april':
        new_challenge = challenges[3]
    elif month.lower() == 'may':
        new_challenge = challenges[4]
    elif month.lower() == 'june':
        new_challenge = challenges[5]
    elif month.lower() == 'july':
        new_challenge = challenges[6]
    else:
        return HttpResponseNotFound('This month challenge is not yet set')
    
    return HttpResponse(new_challenge)