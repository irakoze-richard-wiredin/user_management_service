from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseBadRequest
from django.contrib import messages
from django.contrib.auth import authenticate, login

import jwt
from django.conf import settings
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from data_models.models import UserProfile, AccountVerification, Notifications


from .forms import CustomUserCreationForm, CustomPasswordResetForm

User = get_user_model()

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('account')
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')

    return render(request, 'admin/login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            UserProfile.objects.create(user=user)
            AccountVerification.objects.create(user=user)
            
            return redirect('account')
    else:
        form = CustomUserCreationForm()

    return render(request, 'admin/register.html', {'form': form})



def password_reset(request):
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(email=email).first()

            if user:
                token_data = {'user_id': user.id}
                token = jwt.encode(token_data, settings.SECRET_KEY, algorithm='HS256')

                uidb64 = urlsafe_base64_encode(force_bytes(user.id))

                reset_link = reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
                reset_url = request.build_absolute_uri(reset_link)
                
                Notifications.objects.create(
                    recipient=email,
                    status='pending',
                    subject='Password Reset',
                    body=f'Use the following link to reset your password: {reset_url}',
                )

                # send_mail(
                #     'Password Reset',
                #     f'Use the following link to reset your password: {reset_url}',
                #     'from@example.com',
                #     [email],
                #     fail_silently=False,
                # )

                return render(request, 'admin/password_reset_done.html')
            else:
                messages.error(request, 'No user found with the provided email address.')
    else:
        form = CustomPasswordResetForm()

    return render(request, 'admin/reset_password.html', {'form': form})



def password_reset_confirm(request, uidb64, token):
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    user_id = payload['user_id']
    user = User.objects.get(pk=user_id)

    if user:
        if request.method == 'POST':
            password = request.POST.get('new_password')
            user.set_password(password)
            user.save()

            messages.success(request, 'Password reset successful.')
            login_url = reverse('user_login')
            return redirect(login_url)
        else:
            return render(request, 'admin/reset_password_form.html', {'uidb64': uidb64, 'token': token})
    else:
        return HttpResponseBadRequest('Invalid reset link.')