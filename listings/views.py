from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from property_collections.models import PropertyCollection
from .models import Property, Favorite
from .forms import PropertyForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PropertySerializer
from achievements.models import UserBadge

from django.http import HttpResponse

def presentation_page(request):
    return render(request, 'presentation/presentation.html')

@login_required
def generate_presentation(request, pk):
    return HttpResponse(f'здесь будет преза объекта {pk}')

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

@api_view(['GET'])
def property_detail_api(request, pk):
    property = get_object_or_404(Property, pk=pk)
    serializer = PropertySerializer(property)
    return Response(serializer.data)

# Главная страница со списком объектов
PROPERTY_SORT_OPTIONS = [
    ('newest', 'Сначала новые', '-created_at'),
    ('price_desc', 'По убыванию цены', '-price'),
    ('price_asc', 'По возрастанию цены', 'price'),
    ('oldest', 'Сначала старые', 'created_at'),
    ('title_asc', 'По алфавиту', 'title'),
]


def property_list(request):
    queryset = Property.objects.filter(is_available=True)

    search_query = request.GET.get('q', '').strip()
    if search_query:
        queryset = queryset.filter(
            Q(title__icontains=search_query)
            | Q(description__icontains=search_query)
            | Q(city__icontains=search_query)
            | Q(country__icontains=search_query)
        )

    sort_key = request.GET.get('sort', PROPERTY_SORT_OPTIONS[0][0])
    sort_map = {value: ordering for value, _label, ordering in PROPERTY_SORT_OPTIONS}
    ordering = sort_map.get(sort_key, PROPERTY_SORT_OPTIONS[0][2])
    queryset = queryset.order_by(ordering)

    properties = list(queryset)
    selected_sort = sort_key if sort_key in sort_map else PROPERTY_SORT_OPTIONS[0][0]

    context = {
        'properties': properties,
        'search_query': search_query,
        'selected_sort': selected_sort,
        'sort_options': [
            {'value': value, 'label': label}
            for value, label, _ordering in PROPERTY_SORT_OPTIONS
        ],
        'results_count': len(properties),
        'filters_active': bool(search_query) or selected_sort != PROPERTY_SORT_OPTIONS[0][0],
    }

    return render(request, 'listings/property_list.html', context)

# Детали объекта
@login_required
def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    is_favorite = Favorite.objects.filter(user=request.user, property=property).exists()
    user_badges = UserBadge.objects.filter(user=request.user)
    collections = PropertyCollection.objects.filter(user=request.user)
    return render(request, 'listings/property_detail.html', {
        'property': property,
        'is_favorite': is_favorite,
        'user_badges': user_badges,
        'collections': collections,
    })

