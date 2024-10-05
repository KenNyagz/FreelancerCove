from django.shortcuts import render

def sign_up(request):
    '''sign_in view'''
    return render(request, 'sign-up.html')

def login(request):
    '''login view'''
    return render(request, 'login.html')

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