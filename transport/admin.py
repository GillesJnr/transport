from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


# class UsersAdmin(admin.ModelAdmin):
#     list_display = ('id','name','email','password','group_id','user_type','is_staff','is_active','api_token','last_login')

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
    list_display = ('bookingincome_user','booking_id', 'income_id', 'created_at')

class BookingsAdmin(admin.ModelAdmin):
    list_display = ('customer', 'driver', 'vehicle', 'dest_addr', 'pickup_addr', 'note', 'duration', 'status', 'travellers')

class BookingsMetaAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'type', 'booking_id')

class DriverVehicleAdmin(admin.ModelAdmin):
    list_display = ('created_at','vehicle_id','driver_id')


class EmailContentAdmin(admin.ModelAdmin):
    list_display = ('key', 'value','created_at', 'updated_at')

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('comment','expense_type', 'expense_user','exp_id', 'date' ,'created_at')

class ExpenseCatAdmin(admin.ModelAdmin):
    list_display = ('name','user_id','type','created_at')

class FareSettingsAdmin(admin.ModelAdmin):
    list_display = ('key_name','key_value','created_at')

class FuelAdmin(admin.ModelAdmin):
    list_display = ('fuel_from','province', 'cost_per_unit','vendor','note', 'qty', 'vehicle', 'start_meter','end_meter','reference')

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('income_user','amount','vehicle', 'income_type','mileage', 'date' ,'created_at')


class IncomeCatAdmin(admin.ModelAdmin):
    list_display = ('name','incomecat_user','type', 'created_at')

class VendorTypeAdmin(admin.ModelAdmin):
    list_display = ('type', )


class NotesAdmin(admin.ModelAdmin):
    list_display = ('note','note_vehicle','status','submitted_on','in_charge')	

class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('id','type','notifiable_type','data','notifiable_id','created_at', 'read_at')					


class ReasonsAdmin(admin.ModelAdmin):
    list_display = ('reason','created_at')

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('ratings','review_text','user_id','created_at')		

class ServiceItemsAdmin(admin.ModelAdmin):
    list_display = ('description','time_interval','created_at','overdue_time','overdue_unit','meter_interval','overdue_meter','show_time','show_meter','duesoon_time','duesoon_unit','duesoon_meter')

class ServiceReminderAdmin(admin.ModelAdmin):
    list_display = ('sr_vehicle','sr_service','last_date','last_meter','created_at')

class UsersAdmin(admin.ModelAdmin):
    list_display = ('name','user_image','address','phone_number','user_type','group_id','api_token','created_at')
    exclude = ('id',)

class UsersMetaAdmin(admin.ModelAdmin):
    list_display = ('type','key','value','user_id','created_at')

class VehicleGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'note')

class VehiclesAdmin(admin.ModelAdmin):
    list_display = ('make','model','type','year', 'group' ,'engine_type','vehicle_image')

class VehiclesMetaAdmin(admin.ModelAdmin):
    list_display = ('type','key','value','vehicle_id','created_at')

class VendorsAdmin(admin.ModelAdmin):
    list_display = ('name','photo','type','website','note','phone','address1','city','email')

class WorkOrderAdmin(admin.ModelAdmin):
    list_display= ('status','note','description','price','wo_vehicle', 'wo_vendor')

class EngineTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class WorkOrderStatusAdmin(admin.ModelAdmin):
    list_display = ('name',)


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
admin.site.register(WorkOrders, WorkOrderAdmin)
admin.site.register(ServiceReminder, ServiceReminderAdmin)
admin.site.register(EngineType, EngineTypeAdmin)
admin.site.register(WorkOrderStatus, WorkOrderStatusAdmin)
admin.site.register(VendorType, VendorTypeAdmin)