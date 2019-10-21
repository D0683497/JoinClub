from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import TeaForm, CheckinForm, EditForm
from .models import Tea, Status

def form(request):
    form = TeaForm()
    if request.method == 'POST':
        form = TeaForm(request.POST.copy()) #因要將學號變成大寫，且原本的內容禁止更動，所以用複製的
        form.data['nid'] = form.data['nid'].upper()
        if form.is_valid():
            nid = form.cleaned_data.get('nid')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            """
            判斷 Status 是否有 已填表單
            若有，則在表單資料上添加
            若無，則創建之後添加
            """
            if Status.objects.filter(name="已填表單").exists():
                obj = Tea.objects.create(nid=nid, first_name=first_name, last_name=last_name)
                obj.status.add(Status.objects.get(name="已填表單"))
            else:
                status_obj = Status.objects.create(name="已填表單")
                obj = Tea.objects.create(nid=nid, first_name=first_name, last_name=last_name)
                obj.status.add(status_obj)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = TeaForm()
    return render(request, 'teaform.html', {'form': form})

def checkin(request):
    if request.method == 'POST':
        if 'scan' in request.POST:
            scanform = CheckinForm(request.POST.copy(), prefix='scan')
            keyinform = CheckinForm(prefix='keyin')

            scanform.data['scan-nid'] = scanform.data['scan-nid'][:-1].upper() #學號轉成大寫且去掉最後一個字(掃描機會自動在最後加0)

            if scanform.is_valid():
                nid = scanform.cleaned_data.get('nid')

                if Status.objects.filter(name="已簽到").exists(): #檢查資料庫是否有已簽到狀態
                    status_obj = Status.objects.get(name="已簽到")
                else:
                    status_obj = Status.objects.create(name="已簽到")
                
                if Tea.objects.filter(nid=nid).exists(): #檢查是否填過表單
                        obj = Tea.objects.get(nid=nid)
                        obj.status.add(status_obj)
                else:
                    tea_obj = Tea.objects.create(nid=nid)
                    tea_obj.status.add(status_obj)

                scanform = CheckinForm(prefix='scan')
                return HttpResponseRedirect(reverse('tea-prize', args=[nid]))

        elif 'keyin' in request.POST:
            keyinform = CheckinForm(request.POST.copy(), prefix='keyin')
            scanform = CheckinForm(prefix='scan')

            keyinform.data['keyin-nid'] = keyinform.data['keyin-nid'].upper() #學號轉成大寫

            if keyinform.is_valid():
                nid = keyinform.cleaned_data.get('nid')

                if Status.objects.filter(name="已簽到").exists(): #檢查資料庫是否有已簽到狀態
                    status_obj = Status.objects.get(name="已簽到")
                else:
                    status_obj = Status.objects.create(name="已簽到")
                
                if Tea.objects.filter(nid=nid).exists(): #檢查是否填過表單
                        obj = Tea.objects.get(nid=nid)
                        obj.status.add(status_obj)
                else:
                    tea_obj = Tea.objects.create(nid=nid)
                    tea_obj.status.add(status_obj)
                keyinform = CheckinForm(prefix='keyin')
            
            return HttpResponseRedirect(reverse('tea-prize', args=[nid]))
    else:
        scanform = CheckinForm(prefix='scan')
        keyinform = CheckinForm(prefix='keyin')
    return render(request, 'teacheckin.html', {'scanform': scanform, 'keyinform': keyinform})

def prize(request, nid):
    tea = get_object_or_404(Tea, nid=nid)

    singin_obj = Status.objects.get(name="已簽到")
    if Status.objects.filter(name="已填表單").exists(): #檢查資料庫是否有已填表單狀態
        form_obj = Status.objects.get(name="已填表單")
    else:
        form_obj = Status.objects.create(name="已填表單")

    if Status.objects.filter(name="已領獎").exists(): #檢查資料庫是否有已領獎狀態
        get_obj = Status.objects.get(name="已領獎")
    else:
        get_obj = Status.objects.create(name="已領獎")
    if Status.objects.filter(name="使用票劵領獎").exists(): #檢查資料庫是否有使用票劵領獎狀態
        tix_obj = Status.objects.get(name="使用票劵領獎")
    else:
        tix_obj = Status.objects.create(name="使用票劵領獎")
    
    if request.method == 'POST':
        if 'tix' in request.POST:
            tea.status.add(get_obj)
            tea.status.add(tix_obj)
        elif 'confirm' in request.POST:
            tea.status.add(get_obj)
        elif 'mix' in request.POST:
            tea.status.add(get_obj)
            tea.status.add(tix_obj)
    
    return render(request, 'teaprize.html', {'tea': tea, 'singin_obj': singin_obj, 'form_obj': form_obj, 'get_obj': get_obj})

def show(request):
    tea = Tea.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(tea, 7)
    try:
        teas = paginator.page(page)
    except PageNotAnInteger:
        teas = paginator.page(1)
    except EmptyPage:
        teas = paginator.page(paginator.num_pages)
    return render(request, 'teashow.html', {'teas': teas})

def search(request):
    if request.method == 'POST':
        nid = request.POST.get('nid').upper()
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        
        if nid:
            result = Tea.objects.filter(nid__contains=nid).all()
            print(type(result))
            return render(request, 'teasearch.html', {'result': result})
        elif last_name:
            result = Tea.objects.filter(last_name__contains=last_name).all()
            return render(request, 'teasearch.html', {'result': result})
        elif first_name:
            result = Tea.objects.filter(first_name__contains=first_name).all()
            return render(request, 'teasearch.html', {'result': result})
    return render(request, 'teasearch.html', {})

def edit(request, nid):
    tea = get_object_or_404(Tea, nid=nid)
    form = EditForm(instance=tea)
    if request.method == 'POST':
        form = EditForm(request.POST.copy(), instance=tea)
        form.data['nid'] = form.data['nid'].upper()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tea-view', args=[form.data['nid']]))
    return render(request, 'teaedit.html', {'tea': tea, 'form': form})

def view(request, nid):
    tea = get_object_or_404(Tea, nid=nid)
    return render(request, 'teaview.html', {'tea': tea})

def delete(request, nid):
    tea = get_object_or_404(Tea, nid=nid)
    tea.delete()
    return HttpResponseRedirect(reverse('tea-show'))
