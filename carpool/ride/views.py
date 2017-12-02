from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime as dt
from django.contrib.auth.decorators import login_required
from .forms import NewProfileForm

# Create your views here.


def index(request):
    return render(request, 'all-rides/index.html')


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
@login_required(login_url='/accounts/login/')
def profile(request, profile_id):
    return render(request, 'all-rides/profile.html')


from .email import send_welcome_email


def ride_today(request):
    if request.method == 'POST':
        form = CarRideForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = CarRideRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)

            HttpResponseRedirect('ride_today')
            #.................
    return render(request, 'all-ride/today-ride.html', {"date": date, "ride": ride, "letterForm": form})


@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.editor = current_user
            profile.save()
    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})
