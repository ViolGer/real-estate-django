from gc import get_objects

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Property
from .forms import PropertyForm

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
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            new_property = form.save(commit=False)
            new_property.owner = request.user
            new_property.save()
            return redirect('dashboard')
    else:
        form = PropertyForm()
    return render(request, 'listings/add_property.html', {'form': form})
def edit_property(request, pk):
    property = get_object_or_404(Property, pk=pk, owner=request.user)

    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PropertyForm(instance=property)

    return render(request, 'listings/edit_property.html', {'form': form})
def delete_property(request, pk):
    property = get_object_or_404(Property, pk=pk, owner=request.user)

    if request.method == 'POST':
        property.delete()
        return redirect('dashboard')

    return render(request, 'listings/delete_property.html', {'property': property})