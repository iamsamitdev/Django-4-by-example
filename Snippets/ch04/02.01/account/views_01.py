from django.http import HttpResponse                                           # new
from django.shortcuts import render
from django.contrib.auth import authenticate, login                            # new
from .forms import LoginForm                                                   # new

# new block
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is None:
                return HttpResponse('Invalid login')
            if user.is_active:
                login(request, user)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Disabled account')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})
#
