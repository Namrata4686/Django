#this file created by - namrata
from django.contrib import messages

from django.shortcuts import render
from django.contrib.auth.models import User, auth


def home(request):
    return render(request ,'home.html')


def dashboard(request):
    return render(request ,'Dashboard.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']

        user =auth.authenticate(username=username,password=password)

        if user is not None :
            auth.login(request,user)
            print('Login succesfully....')
            messages.info(request, 'Login succesfully....')
            return render(request , 'dashboard.html')
        else:
            print('Invalid Login credentials')
            messages.info(request ,'Invalid Login credentials')
            return render(request , 'login.html')
    else:
        return render(request ,'login.html')

def signup(request):

    if request.method == 'POST':
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        EmailId = request.POST['EmailID']
        MobileNumber = request.POST['MobileNumber']
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username= username, password= password , email=EmailId , first_name =FirstName , last_name =LastName)
        user.save()
        print('user created')
        messages.info(request, 'Registration completed successfully..........')

        return render(request, 'login.html')
    else:
        return render(request,'signup.html')