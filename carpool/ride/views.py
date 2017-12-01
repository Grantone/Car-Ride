from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime as dt

# Create your views here.


def index(request):
    return render(request, 'profiles/index.html')


def ride_of_day(request):
    date = dt.date.today()
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)


def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', "Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day


# def search_results(request):
#     if '' in request.GET and request.GET["car"]:
#         search_term = request.GET.get("")
#         searched_cars = Car.search_by_title(search_term)
#         message = f"{search_term}"
#
#         return render(request, 'profiles/search.html', {"message": message, "car": searched_cars})
#
#     else:
#         message = "You haven't searched for any car ride"
#         return render(request, 'profiles/search.html', {"message": message})

def profile(request, profile_id):
    return render(request, 'all-rides/profile.html')
