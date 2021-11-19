from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .models import AccountDetail, Verify


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = Verify
#         fields = ['proof_of_identity']

# PROOFS
class ProofOfIdentity(forms.ModelForm):
    class Meta:
        model = Verify
        fields = ['proof_of_identity']
        

class ProofOfResidence(forms.ModelForm):
    class Meta:
        model = Verify
        fields = ['proof_of_residence']
        

class ProofOfAccount(forms.ModelForm):
    class Meta:
        model = Verify
        fields = ['proof_of_account']
        


