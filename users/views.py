from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from users.forms import UserForm, ProfileForm

from listings.models import Property


@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'users/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def profile_view(request):
    user = request.user
    user_properties = Property.objects.filter(owner=user)
    return render(request, 'users/profile.html', {
        'user': user,
        'property_count': user_properties.count()
    })