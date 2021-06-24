from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def registration(request):
    form = UserCreationForm
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            #return redirect('login')
        else:
            form= UserCreationForm
    return render(request, 'registration/register.html', {'form':form})

@login_required
def home(request):
    return render(request, 'anything/home.html')