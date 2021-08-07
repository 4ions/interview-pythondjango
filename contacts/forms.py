from django import forms
from contacts.models import Users, Enterprise

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"

class AddCompanyForm(forms.ModelForm):
    class Meta:
        model= Enterprise
        fields = "__all__"