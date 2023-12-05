# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from data_models.models import UserProfile, AccountVerification
from django.contrib import messages
from .forms import UserProfileForm, AccountVerificationForm

@login_required(login_url='user_login')
def account(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    user_verification = AccountVerification.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            # Redirect or add success message
            
            
            messages.success(request, 'Profile updated successfully.')
            return redirect('account')
    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        'user_profile': user_profile,
        'marital_status_choices': UserProfile.marital_status.field.choices,
        'gender_choices': UserProfile.gender.field.choices,
        'user_verification': user_verification.verification_status,
        'form': form
    }
    return render(request, 'admin/base_site.html', context)



@login_required(login_url='user_login')
def account_verification(request):
    user_verification = AccountVerification.objects.get(user=request.user)

    if request.method == 'POST':
        form = AccountVerificationForm(request.POST, request.FILES, instance=user_verification)
        form.instance.verification_status = 'pending'
        if form.is_valid():
            form.save()
            return redirect('account')
        else:
            return redirect('account')