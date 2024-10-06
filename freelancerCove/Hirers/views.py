from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect#redirect
from .models import Hirer

def sign_up(request):
    '''sign_in view'''
    return render(request, 'sign-up.html')

def login(request):
    '''login view'''
    return render(request, 'login.html')

@csrf_exempt # Disable CSRF protection -for testing
def verify_signup(request):
    '''Function to handle new hirer registration'''
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email= redirect.POST['email']
        password = request.POST['password']
        hashed_password = make_password(password)
        # other fields to be prompted later on, into the app

        new_hirer = Hirer(
                          firstName=firstname,
                          lastName=lastname,
                          email_address=email,
                          hashed_password=hashed_password
        )
        new_hirer.save()
        return HttpResponseRedirect('/hiring/login')
    else:
        return "forbidden", 403

def verify_login(request):
    '''Function to handle user verification'''
    pass

def freelancers_list(request):
    '''View to display available freelancers for hirer'''
    pass

def freelancer_details(request):
    '''View to display details of  selected freelancer'''
    # Include: Freelancer price and/or rate, technologies and specialties of freelancer
    pass

def messages(request):
    '''View for displaying messages for logged in hirer'''
    pass
    # May be a future implementation