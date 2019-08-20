from django.shortcuts import render
from .forms import JoinForm

def index(request):
    return render(request, 'index.html', {})

def join(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = JoinForm()
    return render(request, 'join.html', {'form': form})