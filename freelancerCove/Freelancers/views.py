from django.shortcuts import render
from django.template import loader

def sign_up(request):
    '''sign_in view'''
    return render(request, "sign-up.html")
    

def login(request):
    '''login view'''
    return render(request, 'login.html')

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