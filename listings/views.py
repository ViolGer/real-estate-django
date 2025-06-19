from gc import get_objects

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Property

#обработка запросов на главную страницу
def property_list(request):
    #получаем доступные объекты
    properties = Property.objects.filter(is_available=True).order_by('-created_at')
    #передаем их в шаблон
    return render(request, 'listings/property_list.html', {'properties': properties})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'listings/property_detail.html', {'property': property})


@login_required
def dashboard(request):
    properties = Property.objects.filter(owner=request.user)
    return render(request, 'listings/dashboard.html', {'properties': properties})
