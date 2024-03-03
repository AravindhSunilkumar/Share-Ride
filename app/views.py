from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth import login, authenticate
from .forms import ProfileForm ,UserProfileForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import vehicle_owner
from django.contrib import messages
import os
from django.urls import reverse
# Create your views here.

def index(request):
    owners = vehicle_owner.objects.all()
    return render(request, 'index.html', {'owners': owners})



def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Using the correct login function
            return redirect('home')
        else:
            return redirect('signup')
        
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = first_name
        myuser.save()
        return redirect('login')

        
    return render(request, 'signup.html')

def logoutpage(request):
    logout(request)
    return redirect('login')

def booking(request):
    return render(request, 'booking.html')

def log(request):
    return render(request, 'log.html')

def profile(request):
    user_profile, created_user_profile = Profile.objects.get_or_create(user=request.user)
    
    # Using filter instead of get to handle multiple objects
    additional_profiles = add_profile.objects.filter(user=request.user)

    return render(request, "profile.html", {'user_profile': user_profile, 'additional_profiles': additional_profiles, 'user_id': user_profile.user_id})





def driver(request):
    return render(request,'driver/driver.html')


def dlogin(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Using the correct login function
            return redirect('view_booking')
        else:
            return redirect('dsignup')
        
    return render(request, 'driver/dlogin.html')

def dsignup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = first_name
        myuser.save()
        return redirect('dlogin')

        
    return render(request, 'driver/dsignup.html')


def dlogoutpage(request):
    logout(request)
    return redirect('dlogin')


def user_profile(request):
     
    if request.method=='POST':
        if request.user.is_authenticated:
            user_id = request.user.id
            img=request.FILES['img']
            name=request.POST['name']
            phone_no=request.POST['phone_no']
            
            myprofile=add_profile(user_id=user_id,name=name,phone_number=phone_no,profileimg=img)
            myprofile.save()
            return redirect('profile')
            
    return render(request,'add_profile.html')


def update_profile(request, user_id):
    profile = get_object_or_404(add_profile, user_id=user_id)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'update.html', {'form': form, 'profile': profile})  

# def profile_detail(request, user_id):
#     profile = get_object_or_404(add_profile, user_id=user_id)
#     return render(request, 'profile_detail.html', {'profile': profile})

def driver_profile(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user_id = request.user.id
            img = request.FILES['img']
            name = request.POST['name']
            phone_no = request.POST['phone_no']
            

            myprofile = add_profile(user_id=user_id, name=name, phone_number=phone_no, profileimg=img,
                       )
            myprofile.save()
            return redirect('view_driver')

    return render(request, 'driver/add_driver.html')

def view_driver(request):
    if request.user.is_authenticated:
        user_profiles = add_profile.objects.filter(user=request.user)

        if user_profiles.exists():
            user_profile = user_profiles.first()
            return render(request, 'driver/driver_profile.html', {'user_profile': user_profile})
        else:
            return render(request, 'driver/driver_profile.html')
    else:
        return render(request, 'driver/driver_profile.html')
    
#  update driver
def update_driver(request):
    if request.user.is_authenticated:
        user_profile = add_profile.objects.filter(user=request.user).first()

        if request.method == 'POST':
            form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
            if form.is_valid():
                form.save()
                return redirect('view_driver')  # Redirect to the profile view after a successful update
        else:
            form = UserProfileForm(instance=user_profile)

        return render(request, 'driver/driver_update.html', {'form': form})
    else:
        return render(request, 'driver/driver_profile.html')
    
    # add booking view driver profile
def adddriver_profile(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user_id = request.user.id
            img = request.FILES['img']
            name = request.POST['name']
            phone_no = request.POST['phone_no']
            vehicle_name = request.POST['vehicle_name']
            vehicle_number = request.POST['vehicle_no']  # Make sure this matches your HTML form
            vehicle_img = request.FILES['vehicle_img']

            myprofile = vehicle_owner(user_id=user_id, name=name, phone_number=phone_no, profileimg=img,
                        vehicle_name=vehicle_name, vehicle_img=vehicle_img, vehicle_number=vehicle_number)
            myprofile.save()
            return redirect('booking_dpro')

    return render(request, 'driver/adddriver_pro.html')

# def booking_dpro(request):
#     owners = vehicle_owner.objects.all()
#     return render(request, 'driver/viewdriver_profile.html', {'owners': owners})

def booking_dpro(request):
    if request.user.is_authenticated:
        user_profiles = vehicle_owner.objects.filter(user=request.user)

        if user_profiles.exists():
            user_profile = user_profiles.first()
            return render(request, 'driver/viewdriver_profile.html', {'user_profile': user_profile})
        else:
            return render(request, 'driver/viewdriver_profile.html')
    else:
        return render(request, 'driver/viewdriver_profile.html')
    
def booking(request, pk):
    book = get_object_or_404(vehicle_owner, pk=pk)

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_name = request.POST.get('user_name')
        user_phone = request.POST.get('uphone_number')
        driver_number = request.POST.get('driver_number')  # Corrected this line
        passenger_count = request.POST.get('passenger_count')
        driver_name = request.POST.get('driver_name')
        driver_id = request.POST.get('driver')
        pickup_point = request.POST.get('pickup_point')
        dropping_point = request.POST.get('dropping_point')
        date = request.POST.get('date')
        
        create = Booking.objects.create(
            user_id=user_id,
            user_name=user_name,
            user_phone=user_phone,
            passenger_count=passenger_count,
            driver_id=driver_id,
            driver_name=driver_name,
            pickup_point=pickup_point,
            dropping_point=dropping_point,
            date=date,
            driver_number=driver_number  # Use the correct variable name here
        )
        create.save()
        return redirect('user_booking')
       
    context = {
        'book': book
    }
    return render(request, 'booking.html', context) 

def view_booking(request):
    user = request.user.id
    bookings = Booking.objects.filter(driver_id=user)

    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        if booking_id:
            # Assuming you have a field 'status' in your Booking model
            booking = Booking.objects.get(pk=booking_id)
            booking.status = True  # Change 'approved' to 'status'
            booking.save()
            return redirect('view_booking')

    return render(request, 'driver/view_booking.html', {'bookings': bookings})

def user_booking(request):
    user=request.user.id
    view=Booking.objects.filter(user_id=user)
    context={
        'view':view
    }
    return render(request,'view_booking.html',context)
