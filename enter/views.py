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

@login_required
def search(request):
    if request.method == 'POST':
        nid = request.POST.get('nid')
        name = request.POST.get('name')
        if nid:
            try:
                attend = Attend.objects.get(nid=nid)
                return render(request, 'enter_search.html', {'attend': attend})
            except Attend.DoesNotExist:
                return render(request, 'enter_search.html', {})
        elif name:
            try:
                attend = Attend.objects.get(name=name)
                return render(request, 'enter_search.html', {'attend': attend})
            except Attend.DoesNotExist:
                return render(request, 'enter_search.html', {})
    return render(request, 'enter_search.html', {})

