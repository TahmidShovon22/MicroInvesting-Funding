from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from user.models import User
from django.db import IntegrityError


def showLandingPage(request):
    if request.method == 'POST':
        if request.POST.get('email') and request.POST.get('password'):
            logUser = authenticate( username = 'alamin',  password = request.POST.get('password'))
    return render(request, 'landing/index.html')


def signUpPage(request):
    if request.method == 'POST':
        if request.POST.get('name') \
            and request.POST.get('cell') \
            and request.POST.get('nid') \
            and request.POST.get('dob') \
            and request.POST.get('email') \
            and request.POST.get('password'):
            
            var = User()
            var.name = request.POST.get('name')
            var.nid = request.POST.get('nid')
            var.dob = request.POST.get('dob')
            var.cell = request.POST.get('cell')
            var.email = request.POST.get('email')
            var.password = request.POST.get('password')
            try:
                var.save()
                messages.success(request, 'We just need to verify your email address before you can access. Verify your email address')
                return redirect('/signup')
            except IntegrityError as e:
                if 'UNIQUE constraint failed' in e.args[0]:
                    messages.error(request, 'It seems that this NID or Email is already associated with another account', )
                    return redirect('/signup')

            
            #return HttpResponseRedirect('/signup/success')
    else:
        return render(request, 'landing/signup.html')