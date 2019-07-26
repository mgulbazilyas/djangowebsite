from django.shortcuts import render

# Create your views here.
from pollapp.forms import UserForm, UserProfileInfoForm


def index(request):
    return render(request, 'firstapp/index.html')

def register(request):

    registered = False

    if request.method =='POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)

            user.save()

            profile = profile_form.save(commit=False)

            profile.user = user
            print(request.FILES)
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']


            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    data_dict = {
        'user_form':user_form,
        'profile_form':profile_form,
        'registered':registered
    }

    return render(request, 'firstapp/registration.html', data_dict)


def about_us(request):
    return render(request,'about.html')

def contact_us(request):
    return render(request,'contact.html')