from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group

# Create your views here.


from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login

def librarian_management(request,action=None):
    if not action:
        if request.user.groups.filter(name="Director").exists() or request.user.is_superuser:
            userlist = User.objects.all()
            return render(request,"librarian_management.html",{ "userlist" : userlist})
        else:
            return HttpResponseRedirect("/")
    elif action == "add":
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User(username=username)
            user.set_password(password)
            user.save()
            user.groups.add(Group.objects.get(name="Librarian"))
            return HttpResponseRedirect("/lib")
        else:
            return render(request,"librarian_management.html",{ "action" : action})
    elif action == "delete":
        if request.method == "POST":
            username = request.POST.get('username')
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                if user.groups.filter(name="Librarian").exists():
                    user.delete()
            return HttpResponseRedirect("/lib")
        else:
            return render(request,"librarian_management.html",{ "action" : action})