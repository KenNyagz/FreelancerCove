from django.shortcuts import render
#from django.template import loader

def landing_page(request):
    '''The View for the landing page'''
    #template = loader.get_template("landing.html")
    return render(request, 'landing.html')