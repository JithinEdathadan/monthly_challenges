from http.client import responses

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponsePermanentRedirect, Http404

from django.shortcuts import render
from django.urls import reverse
monthly_challenges = {
    "january": "workout",
    "february": "diet",
    "march": "learn new stack",
    "april": "idk plan a trip may be for december",
    "may": "save for the trip",
    "jun": "happy bday to me",
    "july": None,
    "august": "chill off",
    "september": "book the trip hotels",
    "october" : "idk man",
    "november": "Happy bday ...",
    "december": "Tip mode on .."
}
# Create your views here.
def index(request):
    months = list(monthly_challenges.keys())
    return render(
        request,
        "challenge/index.html",
        {
            "months":months
        }
    )
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month.lower()]
        #
    except:
        raise Http404()
    return render(
        request,
        "challenge/challenge.html",
        {
            "challenge_text":challenge_text,
            "month": month
        }
    )

from django.http import HttpResponse, HttpResponseNotFound

def monthly_challenge_by_number(request, month):
    if month > 12 or month < 1:
        return HttpResponseNotFound("invalid month")
    months = list(monthly_challenges.keys())
    forward_month = months[month-1]
    redirect_path = reverse("month-challenge",args=[forward_month])
    return HttpResponsePermanentRedirect(redirect_path)
