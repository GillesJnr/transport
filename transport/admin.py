from django.contrib import admin
# from .models import Addresses,Allocation,ApiSettings,AuthPermission,AuthUser,BookingIncome, Bookings
# from .models import BookingsMeta, DriverVehicle, EmailContent, Expense,ExpenseCat, FareSettings, Fuel
from .models import *
# Register your models here.


class AddressAdmin(admin.ModelAdmin):
    list_display = ('address', 'customer_id', 'id')

class AllocationAdmin(admin.ModelAdmin):
    list_display= ('month', 'amount')

class ApiSettingsAdmin(admin.ModelAdmin):
    list_display = ('key_name', 'key_value')

# class AuthPermissionAdmin(admin.ModelAdmin):
#     list_display = ('name', 'content_type_id')

# class AuthUserAdmin(admin.ModelAdmin):
#     list_display = ('username','password','last_login','email', 'first_name','last_name','is_staff', 'date_joined')

class BookingIncomeAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'income_id', 'created_at')

class BookingsAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'dest_addr', 'pickup_addr', 'note', 'duration', 'status', 'travellers', 'user_id')

class BookingsMetaAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'type', 'booking_id')

class DriverVehicleAdmin(admin.ModelAdmin):
    list_display = ('created_at','vehicle_id','driver_id')


class EmailContentAdmin(admin.ModelAdmin):
    list_display = ('key', 'value','created_at', 'updated_at')

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('comment','expense_type', 'user_id','exp_id', 'date' ,'created_at')

class ExpenseCatAdmin(admin.ModelAdmin):
    list_display = ('name','user_id','type','created_at')

class FareSettingsAdmin(admin.ModelAdmin):
    list_display = ('key_name','key_value','created_at')

class FuelAdmin(admin.ModelAdmin):
    list_display = ('fuel_from','province', 'cost_per_unit','vendor_name','note', 'qty', 'vehicle_id', 'user_id')

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('amount','income_id','income_cat', 'user_id','mileage', 'date' ,'created_at')


class IncomeCatAdmin(admin.ModelAdmin):
    list_display = ('name','user_id','type', 'created_at')


class NotesAdmin(admin.ModelAdmin):
    list_display = ('note','vehicle_id','status','submitted_on','customer_id')	

class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('id','type','notifiable_type','data','notifiable_id','created_at', 'read_at')					


class ReasonsAdmin(admin.ModelAdmin):
    list_display = ('reason','created_at')

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('ratings','review_text','user_id','created_at')		

class ServiceItemsAdmin(admin.ModelAdmin):
    list_display = ('description','time_interval','created_at')

class UsersAdmin(admin.ModelAdmin):
    list_display = ('name','email','user_type','group_id','api_token','password','created_at')

class UsersMetaAdmin(admin.ModelAdmin):
    list_display = ('type','key','value','user_id','created_at')

class VehicleGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'note')

class VehiclesAdmin(admin.ModelAdmin):
    list_display = ('make','model','type','year','engine_type','vehicle_image')

class VehiclesMetaAdmin(admin.ModelAdmin):
    list_display = ('type','key','value','vehicle_id','created_at')

class VendorsAdmin(admin.ModelAdmin):
    list_display = ('name','photo','type','website','note','phone','address1','city','email')



admin.site.register(Addresses, AddressAdmin)
admin.site.register(Allocation, AllocationAdmin)
admin.site.register(ApiSettings, ApiSettingsAdmin)
# admin.site.register(AuthPermission, AuthPermissionAdmin)
# admin.site.register(AuthUser, AuthUserAdmin)
admin.site.register(BookingIncome, BookingIncomeAdmin)
admin.site.register(Bookings, BookingsAdmin)
admin.site.register(BookingsMeta, BookingsMetaAdmin)
admin.site.register(DriverVehicle, DriverVehicleAdmin)
admin.site.register(EmailContent, EmailContentAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(ExpenseCat, ExpenseCatAdmin)
admin.site.register(FareSettings, FareSettingsAdmin)
admin.site.register(Fuel, FuelAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(IncomeCat, IncomeCatAdmin)
admin.site.register(Notes, NotesAdmin)
admin.site.register(Notifications, NotificationsAdmin)
admin.site.register(Reasons, ReasonsAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(ServiceItems, ServiceItemsAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(UsersMeta, UsersMetaAdmin)
admin.site.register(VehicleGroup, VehicleGroupAdmin)
admin.site.register(Vehicles, VehiclesAdmin)
admin.site.register(VehiclesMeta, VehiclesMetaAdmin)
admin.site.register(Vendors, VendorsAdmin)