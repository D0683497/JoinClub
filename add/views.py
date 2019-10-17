from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import TeacherForm, LocationForm, CategoryForm
from .forms import DegreeForm, CollegeForm, DepartmentForm, LessonForm
from .forms import AttendeeForm, UserForm

def teacher(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'addteacher.html', {'form': form})

def location(request):
    form = LocationForm()
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'addlocation.html', {'form': form})

def category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'addcategory.html', {'form': form})

def lesson(request):
    if request.method == 'POST':
        if 'degree' in request.POST:
            print('degree')
            degreeform = DegreeForm(request.POST, prefix='degree')
            collegeform = CollegeForm(prefix='college')
            departmentform = DepartmentForm(prefix='department')
            lessonform = LessonForm(prefix='lesson')
            if degreeform.is_valid():
                degreeform.save()
                degreeform = DegreeForm(prefix='degree')
                return HttpResponseRedirect(reverse('index'))
        elif 'college' in request.POST:
            print('college')
            degreeform = DegreeForm(prefix='degree')
            collegeform = CollegeForm(request.POST, prefix='college')
            departmentform = DepartmentForm(prefix='department')
            lessonform = LessonForm(prefix='lesson')
            if collegeform.is_valid():
                collegeform.save()
                collegeform = CollegeForm(prefix='college')
                return HttpResponseRedirect(reverse('index'))
        elif 'department' in request.POST:
            print('department')
            degreeform = DegreeForm(prefix='degree')
            collegeform = CollegeForm(prefix='college')
            departmentform = DepartmentForm(request.POST, prefix='department')
            lessonform = LessonForm(prefix='lesson')
            if departmentform.is_valid():
                departmentform.save()
                departmentform = DepartmentForm(prefix='department')
                return HttpResponseRedirect(reverse('index'))
        elif 'lesson' in request.POST:
            print('lesson')
            degreeform = DegreeForm(prefix='degree')
            collegeform = CollegeForm(prefix='college')
            departmentform = DepartmentForm(prefix='department')
            lessonform = LessonForm(request.POST, prefix='lesson')
            if lessonform.is_valid():
                lessonform.save()
                lessonform = LessonForm(prefix='lesson')
                return HttpResponseRedirect(reverse('index'))
    else:
        degreeform = DegreeForm(prefix='degree')
        collegeform = CollegeForm(prefix='college')
        departmentform = DepartmentForm(prefix='department')
        lessonform = LessonForm(prefix='lesson')
    return render(request, 'addlesson.html', {'degreeform': degreeform, 'collegeform': collegeform, 'departmentform': departmentform, 'lessonform': lessonform})

def attendee(request):
    attendeeform = AttendeeForm(prefix='attendee')
    userform = UserForm(prefix='user')
    if request.method == 'POST':
        attendeeform = AttendeeForm(request.POST.copy(), prefix='attendee')
        attendeeform.data['attendee-nid'] = attendeeform.data['attendee-nid'].upper() #學號轉成大寫
        userform = UserForm(request.POST, prefix='user')
        if attendeeform.is_valid() and userform.is_valid():
            user = userform.save()
            user.set_password(userform['password'])
            user.is_active = False
            user.save()
            attendee = attendeeform.save(commit=False)
            attendee.user = user
            attendee.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'addattendee.html', {'attendeeform': attendeeform, 'userform': userform})
