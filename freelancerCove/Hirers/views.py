from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, HttpResponse #redirect
from .models import Hirer

def sign_up(request):
    '''sign_in view'''
    return render(request, 'h_sign-up.html')

def login(request):
    '''login view'''
    return render(request, 'h_login.html')

@csrf_exempt # Disable CSRF protection -for testing
def verify_signup(request):
    '''Function to handle new hirer registration'''
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email= request.POST['email']
        password = request.POST['password']
        hashed_password = make_password(password)
        # other fields to be prompted later on, into the app

        new_hirer = Hirer(
                          firstName=firstname,
                          lastName=lastname,
                          email_address=email,
                          hashed_password=hashed_password
        )
        try:
            new_hirer.save()
            return HttpResponseRedirect('/hiring/login')
        except IntegrityError:    # Email field is set to unique, hence any duplicate will tell
            message = "User already exists(Hirer)"
            template = loader.get_template('user_exists.html')
            data = { "message" : message}
            return HttpResponse(template.render(data, request))
    else:
        return "forbidden", 403

@csrf_exempt
def verify_login(request):
    '''Function to handle user verification'''
    email = request.POST['email']
    password = request.POST['password']
    try:
        user = Hirer.objects.get(email_address=email)
        if not check_password(password, user.hashed_password):
            return render(request, 'wrong_pwd.html')
        return render(request, 'home.html')
    except Hirer.DoesNotExist:
        return render (request, "user_no_exist.html")

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