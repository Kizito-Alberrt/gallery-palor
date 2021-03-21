from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt

# Create your views here.

def welcome(request):
    return HttpResponse('Welcome to gallery Palor')

def palor_of_day(request):
    date = dt.date.today()
    return render(request, 'all-palor/today-palor.html', {"date": date,})

def convert_dates(dates):
     # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day


def past_days_palor(request,past_date):
    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        raise Http404()
        assert False

    if date== dt.date.today():
        return redirect(palor_of_day)

    return render(request, 'all-palor/past-palor.html', {"date": date})

    

def welcome(request):
    return render(request, 'welcome.html')
    
    