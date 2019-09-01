from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import JoinForm
from .models import Member
import csv, codecs
from django.utils.http import urlquote

def index(request):
    return render(request, 'index.html', {})

def join(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('join:index'))
    else:
        form = JoinForm()
    return render(request, 'join.html', {'form': form})

@login_required
def search(request):
    if request.method == 'POST':
        nid = request.POST.get('nid')
        name = request.POST.get('name')
        if nid:
            try:
                member = Member.objects.get(nid=nid)
                return HttpResponseRedirect(reverse('join:review', args=[member.id]))
            except Member.DoesNotExist:
                return render(request, 'search.html', {})
        elif name:
            try:
                member = Member.objects.get(name=name)
                return HttpResponseRedirect(reverse('join:review', args=[member.id]))
            except Member.DoesNotExist:
                return render(request, 'search.html', {})
    return render(request, 'search.html', {})

@login_required
def review(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        if member.status == 'UR':
            member.status = 'NP'
            member.save()
        elif member.status == 'NP':
            member.status = 'M'
            member.save()
    return render(request, 'review.html', {'member': member})

@login_required
def edit(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        form = JoinForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('join:review', args=[member.id]))
        else:
            return render(request, 'edit.html', {'form': form, 'member': member})
    else:
        form = JoinForm()
    return render(request, 'edit.html', {'form': form, 'member': member})

@login_required
def view(request):
    M_members = Member.objects.filter(status='M')
    NP_members = Member.objects.filter(status='NP')
    UR_members = Member.objects.filter(status='UR')
    return render(request, 'view.html', {'M_members': M_members, 'NP_members': NP_members, 'UR_members': UR_members})

def chart(request):
    return render(request, 'chart.html', {})

@login_required
def export(request):
    members = Member.objects.all()
    response = HttpResponse(content_type='text/csv')
    response.write(codecs.BOM_UTF8)
    response['Content-Disposition'] = 'attachment; filename="%s"' %(urlquote("社員資料.csv"))

    writer = csv.writer(response)
    writer.writerow(['姓名', '學號', '系級', '年級', '手機號碼', '電子郵件', '入社狀態'])
    for member in members:
        writer.writerow([member.name, member.nid, member.dept, member.level, member.phone, member.email, member.get_status_display()])

    return response



