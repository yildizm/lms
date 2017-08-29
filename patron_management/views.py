from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group

# Create your views here.


from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from catalog_management.views import catalog_query
from catalog_management.models import Book, Record

def patron_management(request,action=None):
    if not action:
        if request.user.groups.filter(name="Librarian").exists() or request.user.is_superuser:
            return render(request,"patron_management.html",{ "userlist" : "you may control patrons here"})
        else:
            return HttpResponseRedirect("/")
    elif action == "add":
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User(username=username)
            user.set_password(password)
            user.save()
            user.groups.add(Group.objects.get(name="Patron"))
            return HttpResponseRedirect("/lib")
        else:
            return render(request,"patron_management.html",{ "action" : action})
    elif action == "delete":
        if request.method == "POST":
            username = request.POST.get('username')
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                if user.groups.filter(name="Patron").exists():
                    user.delete()
            return HttpResponseRedirect("/pat")
        else:
            return render(request,"patron_management.html",{ "action" : action})
    elif action == "query":
        if request.user.groups.filter(name="Librarian").exists() or request.user.is_superuser:
            if request.method == "POST":
                user = patron_query(request)
                if user == None:
                    return render(request,"patron_management.html",{ "userlist" : "patron not found"})
                else:
                    render(request,"patron_management.html",{ "userlist" : "the patron is found:"+user.username})
                    return HttpResponseRedirect("/pat/borrow")
            else:
                return render(request,"patron_management.html",{ "action" : action})
            return render(request,"patron_management.html",{ "userlist" : "Query a patron"})
        else:
            return HttpResponseRedirect("/")
    elif action == "borrow":
        if request.method == "POST":
            username = request.POST.get('username')
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                if user.groups.filter(name="Patron").exists():
                    user.delete()
            return HttpResponseRedirect("/pat")
        else:
            return render(request,"patron_management.html",{ "action" : action})
    elif action == "return":
        if request.method == "POST":
            username = request.POST.get('username')
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                if user.groups.filter(name="Patron").exists():
                    user.delete()
            return HttpResponseRedirect("/pat")
        else:
            return render(request,"patron_management.html",{ "action" : action})

def patron_query(request):
    username = request.POST.get('name')
    user = None
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
    return user