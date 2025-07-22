from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import PropertyCollection
from listings.forms import CollectionForm
from listings.models import Property, Favorite
from achievements.models import UserBadge

# Создание новой подборки
@login_required
def create_collection(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.user = request.user
            collection.save()
            return redirect('collection_list')
    else:
        form = CollectionForm()
    return render(request, 'property_collections/create_collection.html', {'form': form})

# Список подборок
@login_required
def collection_list(request):
    collections = PropertyCollection.objects.filter(user=request.user)
    return render(request, 'property_collections/collection_list.html', {
        'collections': collections})

# Детали подборки
@login_required
def collection_detail(request, pk):
    collection = get_object_or_404(PropertyCollection, pk=pk, user=request.user)
    return render(request, 'property_collections/collection_detail.html', {'collection': collection})

# Добавление объекта в подборку
@login_required
def add_to_collection(request, property_id):
    if request.method == 'POST':
        collection_id = request.POST.get('collection_id')
        collection = get_object_or_404(PropertyCollection, id=collection_id, user=request.user)
        property = get_object_or_404(Property, id=property_id)
        collection.properties.add(property)
        return redirect('collection_detail', pk=collection.id)
    else:
        collections = PropertyCollection.objects.filter(user=request.user)
        property = get_object_or_404(Property, id=property_id)
        return  render(request, 'property_collections/add_to_collection.html', {
            'collections': collections,
            'property': property,
        })

# Удаление объекта из подборки
@login_required
def remove_from_collection(request, collection_id, property_id):
    collection = get_object_or_404(PropertyCollection, id=collection_id, user=request.user)
    property = get_object_or_404(Property, id=property_id)
    collection.properties.remove(property)
    return redirect('collection_detail', pk=collection_id)

#редактирование коллекции
"""
@login_required
def edit_collection(request, pk):
    collection = get_object_or_404(PropertyCollection, pk=pk, user=request.user)
    if request.method == 'POST':
        form = CollectionForm(request.POST, instance=collection)
        if form.is_valid():
            form.save()
            return redirect('collection_detail', pk=collection.pk)
        else:
            form = CollectionForm(instance=collection)
            return render(request, 'property_collections/edit_collection.html', {
                'form': form,
                'collection': collection
            })
"""


@login_required
def favorite_properties(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('property')
    properties = [fav.property for fav in favorites]
    return render(request, 'property_collections/favorite_properties.html', {
        'properties': properties
    })

@login_required
def create_collection_empty(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.user = request.user
            collection.save()
            return redirect('collection_list')
    else:
        form = CollectionForm()
    return render(request, 'property_collections/create_collection.html', {'form': form})

