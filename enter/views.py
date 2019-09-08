from django.shortcuts import render, get_object_or_404
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
            return HttpResponseRedirect(reverse('commingsoon'))
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

@login_required
def edit(request, id):
    attend = get_object_or_404(Attend, id=id)
    if request.method == 'POST':
        form = AttendForm(request.POST, instance=attend)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'enter_edit.html', {'form': form, 'attend': attend})
    else:
        form = AttendForm()
    return render(request, 'enter_edit.html', {'form': form, 'attend': attend})

