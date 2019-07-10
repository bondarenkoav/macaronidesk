from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from dashboard.forms import login_form


def mylogin(request):
    form = login_form(request.POST or None)
    if request.POST:
        if form.is_valid():
            if form.user is not None:
                login(request, form.user)
                if not request.user.is_superuser:
                    if request.user.groups.all().count() == 0:
                        return redirect('page_error423')
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {'form': form})
        else:
            return render(request, 'login.html', {'form': form})
    else:
        return render(request, 'login.html', {'form': form})


def mylogout(request):
    logout(request)
    return redirect('login')

@login_required
def index(request):
    return render(request, 'index.html')



