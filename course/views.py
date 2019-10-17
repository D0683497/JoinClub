from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CourseForm, CheckinForm
from .models import Course
from join.models import Member, Attendee

def add(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'courseadd.html', {'form': form})

def show(request):
    course_yet = Course.objects.filter(status="YET").all()
    course_end = Course.objects.filter(status="END").all()
    course_hide = Course.objects.filter(status="HIDE").all()
    return render(request, 'courseshow.html', {'course_yet': course_yet, 'course_end': course_end, 'course_hide': course_hide})

def checkinselect(request):
    courses = Course.objects.all()
    return render(request, 'coursecheckinselect.html', {'courses': courses})

def checkin(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        if 'scan' in request.POST:
            scanform = CheckinForm(request.POST.copy(), prefix='scan')
            keyinform = CheckinForm(prefix='keyin')
            
            scanform.data['scan-nid'] = scanform.data['scan-nid'][:-1].upper()
            
            if scanform.is_valid():
                nid = scanform.cleaned_data.get('nid')

                if Member.objects.filter(nid=nid).exists():
                    member = Member.objects.filter(nid=nid).first()
                    course.members.add(member)
                elif Attendee.objects.filter(nid=nid).exists():
                    attendee = Attendee.objects.filter(nid=nid).first()
                    attendee.members.add(member)
                else:
                    # 跳轉至新增參與者
                    scanform = CheckinForm(prefix='scan')
                    return HttpResponseRedirect(reverse('add-attendee'))
                scanform = CheckinForm(prefix='scan')
            
        elif 'keyin' in request.POST:
            keyinform = CheckinForm(request.POST.copy(), prefix='keyin')
            scanform = CheckinForm(prefix='scan')

            keyinform.data['keyin-nid'] = keyinform.data['keyin-nid'].upper() #學號轉成大寫

            if keyinform.is_valid():
                nid = keyinform.cleaned_data.get('nid')

                if Member.objects.filter(nid=nid).exists(): #是社員
                    member = Member.objects.filter(nid=nid).first()
                    course.members.add(member)
                elif Attendee.objects.filter(nid=nid).exists():
                    attendee = Attendee.objects.filter(nid=nid).first()
                    attendee.members.add(member)
                else: 
                    # 跳轉至新增參與者
                    keyinform = CheckinForm(prefix='keyin')
                    return HttpResponseRedirect(reverse('add-attendee'))
                keyinform = CheckinForm(prefix='keyin')
    else:
        scanform = CheckinForm(prefix='scan')
        keyinform = CheckinForm(prefix='keyin')
    return render(request, 'coursecheckin.html', {'course': course, 'scanform': scanform, 'keyinform': keyinform})
