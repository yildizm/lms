from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group

# Create your views here.


from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from catalog_management.models import Book, Record

def catalog_management(request,action=None):
    if not action:
        if request.user.groups.filter(name="Librarian").exists() or request.user.is_superuser:
            return render(request,"catalog_management.html",{ "userlist" : "Welcome to catalog management"})
        else:
            return HttpResponseRedirect("/")
    elif action == "add":
        if request.user.groups.filter(name="Librarian").exists() or request.user.is_superuser:
            if request.method == "POST":
                title = request.POST.get('title')
                author = request.POST.get('author')
                isbn = request.POST.get('isbn')
                book_query = catalog_query(request)
                if book_query == None:
                    book = Book(title=title,author=author,isbn=isbn, available=1)
                    book.save()
                else:
                    return render(request,"catalog_management.html",{ "userlist" : "book already added"})
                return HttpResponseRedirect("/cat/")
            else:
                return render(request,"catalog_management.html",{ "action" : action})
        else:
            return HttpResponseRedirect("/")
    elif action == "delete":
        if request.user.groups.filter(name="Librarian").exists() or request.user.is_superuser:
            if request.method == "POST":
                title = request.POST.get('title')
                if Book.objects.filter(title=title).exists():
                    book = Book.objects.get(title=title)
                    if request.user.groups.filter(name="Librarian").exists():
                        book.delete()
                return HttpResponseRedirect("/cat/")
            else:
                return render(request,"catalog_management.html",{ "action" : action})
        else:
            return HttpResponseRedirect("/")
    elif action == "query":
        if request.user.groups.filter(name="Librarian").exists() or request.user.groups.filter(name="Patron").exists() or request.user.is_superuser:
            if request.method == "POST":
                book = catalog_query(request)
                if book == None:
                    return render(request,"catalog_management.html",{ "list" : "book not found"})
                else:
                    return render(request,"catalog_management.html",{ "userlist" : "the book is found:"+book.title})
            else:
                return render(request,"catalog_management.html",{ "action" : action})
            return render(request,"catalog_management.html",{ "userlist" : "Query a book"})
        else:
            return HttpResponseRedirect("/")

def catalog_query(request):
    title = request.POST.get('title')
    book = None
    if Book.objects.filter(title=title).exists():
        book = Book.objects.get(title=title)
    return book
 