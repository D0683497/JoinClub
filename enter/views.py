from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AttendForm
from .models import Attend

@login_required
def attend(request):
    if request.method == 'POST':
        form = AttendForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, '提交成功', extra_tags='attendform')
            return HttpResponseRedirect(reverse('join:commingsoon'))
    else:
        form = AttendForm()
    return render(request, 'attend.html', {'form': form})