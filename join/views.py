from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import JoinForm
from .models import Member

def index(request):
    return render(request, 'index.html', {})

def join(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            Member(name=form['name'].value(), nid=form['nid'].value(), dept=form['dept'].value(), level=form['level'].value(), phone=form['phone'].value(), email=form['email'].value()).save()
            form = JoinForm()
        return HttpResponseRedirect(reverse('index'))
    else:
        form = JoinForm()
    return render(request, 'join.html', {'form': form})