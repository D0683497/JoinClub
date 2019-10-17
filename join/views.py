from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.models import User
from .models import Member, Position
from .forms import MemberForm, UserForm, KeyinForm, ScanForm, EditMemberForm, EditUserForm

def form(request):
    memberform = MemberForm(prefix='member')
    userform = UserForm(prefix='user')
    if request.method == 'POST':
        memberform = MemberForm(request.POST.copy(), prefix='member')
        memberform.data['member-nid'] = memberform.data['member-nid'].upper() #學號轉成大寫
        userform = UserForm(request.POST, prefix='user')
        if memberform.is_valid() and userform.is_valid():
            user = userform.save()
            user.set_password(userform['password'])
            user.is_active = False
            user.save()
            member = memberform.save(commit=False)
            member.user = user
            member.save()
            return HttpResponseRedirect(reverse('index'))

    return render(request, 'joinform.html', {'memberform': memberform, 'userform': userform})

def search(request):
    if request.method == 'POST':
        if 'scan' in request.POST:
            keyinform = KeyinForm()
            scanform = ScanForm(request.POST.copy())

            scanform.data['nid'] = scanform.data['nid'][:-1].upper() #學號轉成大寫且去掉最後一個字(掃描機會自動在最後加0)

            if scanform.is_valid():
                nid = scanform.cleaned_data.get('nid')

                if Member.objects.filter(nid=nid).exists():
                    return HttpResponseRedirect(reverse('join-review', args=[nid]))
            scanform = ScanForm()
        elif 'keyin' in request.POST:
            keyinform = KeyinForm(request.POST.copy())
            scanform = ScanForm()

            keyinform.data['nid'] = keyinform.data['nid'].upper() #學號轉成大寫

            if keyinform.is_valid():
                nid = keyinform.cleaned_data.get('nid')
                username = keyinform.cleaned_data.get('username')
                email = keyinform.cleaned_data.get('email')
                first_name = keyinform.cleaned_data.get('first_name')
                last_name = keyinform.cleaned_data.get('last_name')
                phone = keyinform.cleaned_data.get('phone')
                lesson = keyinform.cleaned_data.get('lesson')

                if nid:
                    memberresult = Member.objects.filter(nid__contains=nid).all()
                    keyinform = KeyinForm()
                    return render(request, 'joinsearch.html', {'keyinform': keyinform, 'scanform': scanform, 'memberresult': memberresult})
                elif username:
                    userresult = User.objects.filter(username__contains=username).all()
                    keyinform = KeyinForm()
                    return render(request, 'joinsearch.html', {'keyinform': keyinform, 'scanform': scanform, 'userresult': userresult})
                elif email:
                    userresult = User.objects.filter(email__contains=email).all()
                    keyinform = KeyinForm()
                    return render(request, 'joinsearch.html', {'keyinform': keyinform, 'scanform': scanform, 'userresult': userresult})
                elif first_name:
                    userresult = User.objects.filter(first_name__contains=first_name).all()
                    keyinform = KeyinForm()
                    return render(request, 'joinsearch.html', {'keyinform': keyinform, 'scanform': scanform, 'userresult': userresult})
                elif last_name:
                    userresult = User.objects.filter(last_name__contains=last_name).all()
                    keyinform = KeyinForm()
                    return render(request, 'joinsearch.html', {'keyinform': keyinform, 'scanform': scanform, 'userresult': userresult})
                elif phone:
                    memberresult = Member.objects.filter(phone__contains=phone).all()
                    keyinform = KeyinForm()
                    return render(request, 'joinsearch.html', {'keyinform': keyinform, 'scanform': scanform, 'memberresult': memberresult})
                elif lesson:
                    memberresult = Member.objects.filter(lesson=lesson).all()
                    keyinform = KeyinForm()
                    return render(request, 'joinsearch.html', {'keyinform': keyinform, 'scanform': scanform, 'memberresult': memberresult})
            keyinform = KeyinForm()
        else:
            nid = request.POST.get('nid').upper()
            memberresult = Member.objects.filter(nid__contains=nid).all()
            keyinform = KeyinForm()
            scanform = ScanForm()
            return render(request, 'joinsearch.html', {'keyinform': keyinform, 'scanform': scanform, 'memberresult': memberresult})
    else:
        keyinform = KeyinForm()
        scanform = ScanForm()

    return render(request, 'joinsearch.html', {'keyinform': keyinform, 'scanform': scanform})

def view(request, nid):
    member = get_object_or_404(Member, nid=nid)
    return render(request, 'joinview.html', {'member': member})

def review(request, nid):
    member = get_object_or_404(Member, nid=nid)
    if request.method == 'POST':
        if 'confirm' in request.POST:
            member.status = 'NP'
            member.save()
        elif 'pay' in request.POST:
            position_obj, created = Position.objects.get_or_create(name="社員")
            member.status = 'M'
            member.positions = position_obj
            member.save()
            member.user.is_active = True
            member.user.save()
    return render(request, 'joinreview.html', {'member': member})

def show(request):
    member = Member.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(member, 7)
    try:
        members = paginator.page(page)
    except PageNotAnInteger:
        members = paginator.page(1)
    except EmptyPage:
        members = paginator.page(paginator.num_pages)
    return render(request, 'joinshow.html', {'members': members})

def edit(request, nid):
    member = get_object_or_404(Member, nid=nid)
    memberform = EditMemberForm(instance=member)
    userform = EditUserForm(instance=member.user)
    if request.method == 'POST':
        memberform = EditMemberForm(request.POST.copy(), instance=member)
        userform = EditUserForm(request.POST, instance=member.user)
        memberform.data['nid'] = memberform.data['nid'].upper()
        if memberform.is_valid() and userform.is_valid():
            memberform.save()
            userform.save()
            nid = memberform.data['nid']
            memberform = EditMemberForm(instance=member)
            userform = EditUserForm(instance=member.user)
            return HttpResponseRedirect(reverse('join-view', args=[nid]))
    return render(request, 'joinedit.html', {'member': member, 'memberform': memberform, 'userform': userform})
