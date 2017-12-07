from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime as dt
from django.contrib.auth.decorators import login_required
from .forms import PassengerForm, DriverForm
from .models import User, Passenger, Driver
from .email import send_welcome_email
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    return render(request, 'all-rides/index.html')


def login_driver(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        driver = authenticate(username=username, password=password)
        if user is not None:
            login(request, driver)
            return redirect('index')

    return render(request, 'registration/login.html', {
        'form': form
    })


def signout(request):
    logout(request)
    return redirect('index')


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
    profile = Profile.objects.get(id=profile_id)
    date = dt.date.today()
    print(date)
    return render(request, 'all-rides/profile.html', {"date": date, "profile": profile})


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

    return render(request, 'all-ride/today-ride.html', {"ride": ride, "letterForm": form})


@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    found_profile = current_user.profile
    if request.method == 'POST':
        form = NewProfileForm(
            request.POST, instance=current_user.profile,  files=request.FILES)
        if form.is_valid():
            update_profile = form.save(commit=False)
            update_profile.user = current_user
            update_profile.save()
            return redirect(profile, found_profile.id)
    else:
        form = NewProfileForm(instance=current_user.profile)
    return render(request, 'new_profile.html', {"form": form})


@login_required
def passenger(request):

    current_user = request.user

    passenger = Passenger.objects.filter(user=current_user)

    form = PassengerForm(request.POST)
    if request.method == 'POST':
        form = PassengerForm(request.POST, request.FILES)
        if form.is_valid():
            passenger = form.save(commit=False)
            passenger.user = request.user
            passenger.save()
            return redirect(passenger_profile, passenger.id)

    else:
        form = PassengerForm(user=current_user)
        return render(request, 'all-rides/passenger.html', {"form": form, "passenger": current_user})

    print('<><><><><>almost<><><><><>')


@login_required
def driver(request):
    current_user = request.user
    print('<><><><><almost there><><><><><>')
    driver = Driver.objects.filter(driver=current_user)

    form = DriverForm(request.POST)
    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES)
        if form.is_valid():
            driver = form.save(commit=False)
            driver.user = request.user
            driver.save()
            return redirect(driver_profile, driver.id)

    else:
        form = DriverForm(user=current_user)
        return render(request, 'all-rides/driver.html', {"form": form, "driver": current_user})

    # return render(request, 'driver.html')


def passenger_profile(request, passenger_id):
    passenger_profile = Profile.objects.get(id=passenger_id)

    return render(request, 'all-rides/passenger_profile.html', {"passenger_profile": passenger_profile})


def driver_profile(request, driver_id):
    driver_profile = Profile.objects.get(id=driver_id)

    return render(request, 'all-rides/driver_profile.html', {"driver_profile": driver_profile})
