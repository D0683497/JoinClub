
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from datetime import datetime, timedelta

class DeadlineMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        if view_func.__module__ == 'django.contrib.admin.sites' or request.user.is_superuser:
                return None
        else:
            survey = datetime(2019, 9, 10, 22, 45, 0, 0) #茶會調查結束時間
            teatime = datetime(2019, 9, 11, 22, 45, 0, 0) #茶會開始時間
            if survey - datetime.now() <= timedelta(milliseconds=0): #調查結束
                if teatime - datetime.now() <= timedelta(milliseconds=0): #調查結束+茶會開始
                    if view_func.__module__ == 'join.views' and view_func.__name__ == 'attend':
                        messages.add_message(request, messages.INFO, '表單已結束提交', extra_tags='teatimeform')
                        return HttpResponseRedirect(reverse('join:index'))
                    elif view_func.__module__ == 'join.views' and view_func.__name__ == 'commingsoon':
                        return HttpResponseRedirect(reverse('join:index'))
                    else:
                        return None
                else: #調查結束+茶會未開始
                    if view_func.__module__ == 'join.views' and view_func.__name__ == 'commingsoon':
                        return None
                    else:
                        if view_func.__module__ == 'join.views' and view_func.__name__ == 'attend':
                            messages.add_message(request, messages.INFO, '表單已結束提交', extra_tags='teatimeform')
                        return HttpResponseRedirect(reverse('join:commingsoon'))
            else: #調查未結束
                if (view_func.__module__ == 'join.views' and view_func.__name__ == 'commingsoon') or (view_func.__module__ == 'join.views' and view_func.__name__ == 'attend'):
                    return None
                return HttpResponseRedirect(reverse('join:commingsoon'))




