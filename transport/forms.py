from django import forms
from django.contrib.auth.models import User
from .models import Users
from django.contrib.auth.forms import UserCreationForm


class CreateLoginForm(forms.Form):
    class Meta:
        model = User
        fields = ['email', 'password']


class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(AddUserForm,self).__init__(*args, **kwargs)
        self.fields['email'].required = True


class AddUsersForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()
    phone_number  =forms.CharField()
    user_image = forms.ImageField()
    group_id = forms.IntegerField()
     
    class Meta:
        model = Users
        fields = ['name','email','address','phone_number','user_image','group_id']

    def __init__(self, *args, **kwargs):
        super(AddUsersForm,self).__init__(*args, **kwargs)
    #     self.fields['user_type'].empty_label = 'Select User Type'
        self.fields['user_image'].required = False
        
    
