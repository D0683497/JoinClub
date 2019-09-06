from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.http import urlquote
import csv, codecs
from join.models import Member

from django.views.generic import View
from django.http import JsonResponse


def joinclub(request):
    All_count = Member.objects.all().count()
    M_count = Member.objects.filter(status='M').count()
    return render(request, 'joinclub.html', {'All_count': All_count, 'M_count': M_count})

class  JoinclubData(View):
    def  get(self, request):
        All_count = Member.objects.all().count()
        M_count = Member.objects.filter(status='M').count()
        data =  {'All_count': All_count, 'M_count': M_count}
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
