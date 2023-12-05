from django import forms
from data_models.models import UserProfile, AccountVerification

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo', 'gender', 'age', 'date_of_birth', 'marital_status', 'nationality']

class AccountVerificationForm(forms.ModelForm):
    class Meta:
        model = AccountVerification
        fields = ['nid_passport_number', 'document_image']