from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404
from listings.models import Property, PropertyImage

def presentation_view(request, pk):
    property_obj = get_object_or_404(Property, id=pk)
    images = PropertyImage.objects.filter(property=property_obj)
    context = {
        'property': property_obj,
        'images': images,
    }
    return render(request, 'presentation/presentation.html', context)