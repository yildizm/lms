from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.


from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login

def login(request):
    if request.POST.get('username') and request.POST.get('password'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                django_login(request, user)
                return HttpResponseRedirect('/')
                # Redirect to a success page.
            else:
                # Return a 'disabled account' error message
                return render(request,"login.html",{ "error_message" : "Authentication failed!"})
        else:
            # Return an 'invalid login' error message.
            return render(request,"login.html",{ "error_message" : "Authentication failed!"})
    else:
        return render(request,"login.html")

def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/')