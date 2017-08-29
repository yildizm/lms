from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):
	if request.user and request.user.is_authenticated():
		return render(request,"home.html")
	else:
		return HttpResponseRedirect('auth/login')