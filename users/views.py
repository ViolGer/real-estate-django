from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserUpdateForm
from listings.models import Property


@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'users/edit_profile.html', {'form': form})
def profile_view(request):
    user = request.user
    user_properties = Property.objects.filter(owner=user)
    return render(request, 'users/profile.html', {
        'user': user,
        'property_count': user_properties.count()
    })