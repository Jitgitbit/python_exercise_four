from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.db import IntegrityError

# Create your views here.
def home(request):
	return render(request, 'todo/home.html')

def signupuser(request):
	if request.method == 'GET':
		return render(request, 'todo/signupuser.html', {'form':UserCreationForm()})
	else:
		# Create a new user
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.create_user(request.POST['username'], request.POST['password1'])
				user.save()
				login(request, user)
				return redirect('currenttodos')
			except IntegrityError:
				return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'That username has been taken already. Please choose a different username'})
		else:
			# Tell the user the passwords didn't match
			return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def currenttodos(request):
	return render(request, 'todo/currenttodos.html')

def logoutuser(request):
	if request.method == 'POST':
		logout(request)
		return redirect('home')