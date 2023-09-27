from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import LocationForm, ProfileForm, UserForm
from main.models import Listing, LikedListing


# Create your views here.
def users_view_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(
                    request, f"you've logged in as {username}"
                )
                return redirect('home')
            else:
                pass
        else:
            messages.error(
                request, 'There was a problem trying to log you in, please try again'
            )
    elif request.method == 'GET':
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})


@login_required
def users_view_logout(request):
    logout(request)
    return redirect('main')


class  UsersViewRegister(View):
    def get(self, request):
        register_form = UserCreationForm()
        return render(request, 'register.html', {'register_form': register_form})
    
    def post(self, request):
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.refresh_from_db()
            login(request, user)
            messages.success(
                request, f"you've logged in as {user.username}"
            )
            return redirect('home')
        else:
            messages.error(
                request, 'There was a problem trying to register you, please try again'
            )
            return render(request, 'register.html', {'register_form': register_form})
        

@method_decorator(login_required, name='dispatch')
class UsersViewProfile(View):

    def get(self, request):

        user_listings = Listing.objects.filter(seller=request.user.profile)
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        location_form = LocationForm(instance=request.user.profile.location)
        liked_listings= LikedListing.objects.filter(profile=request.user.profile).all()

        return render(request, 'profile.html', {'user_form': user_form, 
                                                'profile_form': profile_form, 
                                                'location_form': location_form,
                                                'user_listings': user_listings,
                                                'liked_listings': liked_listings})

    def post(self, request):
        user_listings = Listing.objects.filter(seller=request.user.profile)
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        location_form = LocationForm(request.POST, instance=request.user.profile.location)
        liked_listings= LikedListing.objects.filter(profile=request.user.profile).all()

        if user_form.is_valid() and profile_form.is_valid() and location_form.is_valid():
            user_form.save()
            profile_form.save()
            location_form.save()
            messages.success(request, 'The profile was updated succesfully')
        else:
            messages.error(request, 'Error updating the profile')
        return render(request, 'profile.html', {'user_form': user_form, 
                                                'profile_form': profile_form, 
                                                'location_form': location_form,
                                                'user_listings': user_listings,
                                                'liked_listings': liked_listings})