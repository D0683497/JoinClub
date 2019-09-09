from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.http import urlquote
import csv, codecs
from join.models import Member
from enter.models import Attend, Checkin

from django.views.generic import View
from django.http import JsonResponse

class CommingsoonData(View):
    def get(self, request):
        Attend_count = Attend.objects.all().count()
        data =  {'Attend_count': Attend_count, }
        return JsonResponse(data)

def joinclub(request):
    return render(request, 'joinclub.html', {})

class JoinclubData(View):
    def get(self, request):
        Checkin_count = Checkin.objects.all().count()
        Member_count = Member.objects.all().count()
        M_count = Member.objects.filter(status='M').count()
        data =  {'Checkin_count': Checkin_count, 'Member_count': Member_count, 'M_count': M_count}
        return JsonResponse(data)

def receiveprize(request):
    return render(request, 'receiveprize.html', {})

class ReceiveprizeData(View):
    def get(self, request):
        Checkin_count = Checkin.objects.all().count()
        Tix_count = Checkin.objects.filter(status='TIX').count() #已使用票券領獎
        FORM_count = Checkin.objects.filter(status='FORM').count() #已填表單領獎
        MIX_count = Checkin.objects.filter(status='MIX').count() #已填表單加使用票券領獎
        Prize_count = Tix_count + FORM_count + MIX_count
        data =  {'Checkin_count': Checkin_count, 'Prize_count': Prize_count}
        return JsonResponse(data)


def attendance(request):
    return render(request, 'attendance.html', {})

class AttendanceData(View):
    def get(self, request):
        Attend_count = Attend.objects.all().count()
        Tix_count = Checkin.objects.filter(status='TIX').count() #已使用票券領獎
        NO_count = Checkin.objects.filter(status='NO').count() #已填表單領獎
        Count = Attend_count - Tix_count - NO_count
        data =  {'Attend_count': Attend_count, 'Count': Count}
        return JsonResponse(data)

@login_required
def export_all(request):
    members = Member.objects.all()
    response = HttpResponse(content_type='text/csv')
    response.write(codecs.BOM_UTF8)
    response['Content-Disposition'] = 'attachment; filename="%s"' %(urlquote("社員資料.csv"))
    writer = csv.writer(response)
    writer.writerow(['姓名', '學號', '系級', '年級', '手機號碼', '電子郵件', '入社狀態'])
    for member in members:
        writer.writerow([member.name, member.nid, member.dept, member.level, member.phone, member.email, member.get_status_display()])
    return response

@login_required
def export_M(request):
    members = Member.objects.filter(status='M')
    response = HttpResponse(content_type='text/csv')
    response.write(codecs.BOM_UTF8)
    response['Content-Disposition'] = 'attachment; filename="%s"' %(urlquote("社員資料(已繳費).csv"))
    writer = csv.writer(response)
    writer.writerow(['姓名', '學號', '系級', '年級', '手機號碼', '電子郵件', '入社狀態'])
    for member in members:
        writer.writerow([member.name, member.nid, member.dept, member.level, member.phone, member.email, member.get_status_display()])
    return response

@login_required
def export_NP(request):
    members = Member.objects.filter(status='NP')
    response = HttpResponse(content_type='text/csv')
    response.write(codecs.BOM_UTF8)
    response['Content-Disposition'] = 'attachment; filename="%s"' %(urlquote("社員資料(未繳費).csv"))
    writer = csv.writer(response)
    writer.writerow(['姓名', '學號', '系級', '年級', '手機號碼', '電子郵件', '入社狀態'])
    for member in members:
        writer.writerow([member.name, member.nid, member.dept, member.level, member.phone, member.email, member.get_status_display()])
    return response
