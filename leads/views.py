from django.shortcuts import render, redirect
from .models import Lead
from django.contrib.auth.decorators import login_required

@login_required
def lead_create(request):
    if request.method == 'POST':
        name = request.POST.get('client_name')
        phone = request.POST.get('phone')
        prop = request.POST.get('property_name')
        comment = request.POST.get('comment')
        Lead.objects.create(agent=request.user, client_name=name, phone=phone, property_name=prop, comment=comment)
        return redirect('my_leads')
    return render(request, 'leads/lead_create.html')

@login_required
def my_leads(request):
    leads = Lead.objects.filter(agent=request.user)
    return render(request, 'leads/my_leads.html', {'leads': leads})
