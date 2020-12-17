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
    
    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        super().__init__(**kwargs)


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
        self.fields['status'].empty_label = 'Select Status'


class VendorForm(ModelForm):
    class Meta:
        model = Vendors
        fields = '__all__'
        exclude = ('created_at', 'updated_at', 'deleted_at')

    def __init__(self, *args, **kwargs):
        super(VendorForm, self).__init__(*args, **kwargs)
        self.fields['type'].empty_label = 'Select Type'


class NoteForm(ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'
        exclude = ('created_at', 'updated_at', 'deleted_at')
        widgets = {
            'submitted_on' : DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.fields['in_charge'].empty_label = 'Choose Person in Charge'
        self.fields['in_charge'].label = 'Assign Person'
        self.fields['note_vehicle'].empty_label = 'Select Vehicle'
        self.fields['status'].empty_label = 'Select Status'
        self.fields['in_charge'].queryset = Users.objects.all().exclude(user_type='C')


class ReminderForm(ModelForm):
    class Meta:
        model = ServiceReminder
        fields = '__all__'
        exclude = ('created_at','deleted_at','updated_at')
        widgets = {
             'last_date': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(ReminderForm, self).__init__(*args, **kwargs)
        self.fields['sr_vehicle'].empty_label = 'Select Vehicle'
        self.fields['sr_vehicle'].label = 'Select Vehicle'
        self.fields['sr_service'].label = 'Select Service'
        self.fields['sr_service'].empty_label = 'Select Service'



class ServiceItemForm(ModelForm):
    class Meta:
        model = ServiceItems
        fields = '__all__'
        exclude = ('created_at','updated_at','deleted_at')


class IncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = ('vehicle', 'income_type', 'amount', 'mileage',  'date')
        widgets = {
             'date': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(IncomeForm, self).__init__(*args, **kwargs)
        self.fields['vehicle'].empty_label = 'Select Vehicle'
        self.fields['income_type'].empty_label = 'Select Income Type'

            

class ExpenseForm(ModelForm):
    class Meta: 
        model = Expense
        fields = ('vehicle','expense_type','amount','comment','date')
        widgets = {
            'date': DateInput()
        }
        
    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.fields['vehicle'].empty_label = 'Select Vehicle'
        self.fields['expense_type'].empty_label = 'Select Expense Type'


class BookingForm(ModelForm):
    class Meta:
        model = Bookings
        fields = ('customer','vehicle','driver','pickup','dropoff','pickup_addr','dest_addr','note', 'travellers')
        widgets = {
            'pickup' : DateTimeInput(),
            'dropoff' : DateTimeInput(),
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['customer'].empty_label = 'Select Customer'
        self.fields['vehicle'].empty_label = 'Select Vehicle'
        self.fields['driver'].empty_label = 'Select Driver'
        self.fields['customer'].queryset = Users.objects.all().filter(user_type='C')
        self.fields['driver'].queryset = Users.objects.all().filter(user_type='D')
        self.fields['pickup_addr'].label = "Pick Up Address"
        self.fields['dest_addr'].label = "Destination Address"
        self.fields['pickup'].input_formats = ["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"]
        self.fields['dropoff'].input_formats = ["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"]

        

class FuelForm(ModelForm):
    class Meta:
        model = Fuel
        fields = "__all__"
        exclude = ('created_at','updated_at','deleted_at', 'fuel_from')
        widgets = {
            'date' : DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(FuelForm, self).__init__(*args, **kwargs)
        self.fields['vehicle'].empty_label = 'Select Vehicle'
        self.fields['vendor'].empty_label = 'Select Vendor'
        self.fields['start_meter'].help_text = 'Meter reading at time of fuel up'
