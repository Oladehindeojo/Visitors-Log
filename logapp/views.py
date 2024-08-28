from django.shortcuts import render, redirect
from .forms import VisitorForm
from .models import Visitor

def visitor_sign_in(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logapp:visitor_list')
    else:
        form = VisitorForm()
    return render(request, 'visitor_sign_in.html', {'form': form})

def visitor_list(request):
    visitors = Visitor.objects.all().order_by('-arrival_time')
    return render(request, 'visitor_list.html', {'visitors': visitors})
