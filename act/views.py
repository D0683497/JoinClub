from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import ActivityForm
from .models import Activity

def add(request):
    form = ActivityForm()
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'actadd.html', {'form': form})

def show(request):
    act_singupyet = Activity.objects.filter(status="SINGUPYET").all()
    act_yet = Activity.objects.filter(status="YET").all()
    act_full = Activity.objects.filter(status="FULL").all()
    act_singupend = Activity.objects.filter(status="SINGUPEND").all()
    act_end = Activity.objects.filter(status="END").all()
    act_hide = Activity.objects.filter(status="HIDE").all()
    return render(request, 'actshow.html', {'act_singupyet': act_singupyet, 'act_yet': act_yet, 'act_full': act_full, 'act_singupend': act_singupend, 'act_end': act_end, 'act_hide': act_hide})

