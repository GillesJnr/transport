from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

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
        

class DateInput(forms.DateInput):
    input_type = 'date'
    

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicles
        fields = '__all__'
        exclude = ['created_at', 'updated_at', 'deleted_at']
        widgets = {
            'lic_exp_date': DateInput(),
            'reg_exp_date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
        self.fields['vehicles_user'].queryset = Users.objects.all().filter(user_type='D')
        self.fields['vehicles_user'].empty_label = 'Select Driver'
        self.fields['group'].empty_label = 'Select Group'
        self.fields['engine_type'].empty_label = 'Select Type'



class DateInput(forms.DateInput):
    input_type = 'date'


class VehicleGroupForm(ModelForm):
    class Meta:
        model = VehicleGroup
        fields = '__all__'
        exclude = ('deleted_at','created_at','updated_at')


class WorkOrderForm(ModelForm):
    class Meta:
        model = WorkOrders
        fields = '__all__'
        exclude = ('created_at','updated_at','deleted_at')
        widgets = {
            'created_on': DateInput(),
            'required_by': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(WorkOrderForm, self).__init__(*args, **kwargs)
        self.fields['wo_vendor'].empty_label = 'Select Vendor'
        self.fields['wo_vehicle'].empty_label = 'Select Vehicle'