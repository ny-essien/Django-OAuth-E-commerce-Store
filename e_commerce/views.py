from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout,authenticate

# Create your views here.
def homepage(request):

    return render(request, "e_commerce/home.html")
    

def signin(request):

    if request.user.is_authenticated:
        return redirect('e_commerce:home')

    if request.method == 'POST':

        #Authenticate if user records exist in the database
        user = authenticate(username = request.POST['username'], password = request.POST['password1'] )

        #if an instance of the user is found in the database
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in succesfully')
            return redirect('e_commerce:home')

        else:
            messages.error(request, 'Incorrect Username or Password')
            return redirect('e_commerce:home')


    return render(request, "e_commerce/signin.html")


def signup(request):

    if request.method == 'POST':
        
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        username = request.POST['username']
        email = request.POST['email-address']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']

        user = User.objects.create_user(username= username, email= email , password = password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return redirect('e_commerce:signup')

    return render(request, "e_commerce/signup.html")


def logoutPage(request):

    logout(request)
    return redirect('e_commerce:home')
