from django.shortcuts import render
from django.template import loader
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect, HttpResponse #redirect
from .models import freelancer

def sign_up(request):
    '''sign_in view'''
    return render(request, "sign-up.html")
    

def login(request):
    '''login view'''
    return render(request, 'login.html')

@csrf_exempt # Disable CSRF protection -for testing
def verify_signup(request):
    '''Function to handle new freelancer registration'''
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        hashed_password = make_password(password)
        # other fields to be prompted later on, into the app

        new_freelancer = freelancer(
                                    firstName=firstname,
                                    lastName=lastname,
                                    email_address=email,
                                    hashed_password=hashed_password
        )
        try:
            new_freelancer.save()
            return HttpResponseRedirect('/freelance/login')
        except IntegrityError: # Email field is set to unique, hence any duplicate will tell
            message = "User already exists(Freelancer)"
            template = loader.get_template('user_exists.html')
            data = { "message" : message}
            return HttpResponse(template.render(data, request))
    else:
        return "forbidden", 403

def verify_login(request):
    '''Function to handle user verification'''
    pass

def jobs_list(request):
    '''View to display available jobs for freelancer'''
    pass

def job_details(request):
    '''View to display details of  selected job'''
    # Include: Offer from hirer, particulars hirer is looking for
    pass

def messages(request):
    '''View for displaying messages for logged in freelancer'''
    pass
    # May be a future implementation