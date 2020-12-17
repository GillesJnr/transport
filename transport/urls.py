from django.urls import path
from . import  views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home"),
    path('adduser', views.adduser, name="adduser"),
    path('login', views.login, name = "login"),
    path('logout', views.logout, name = "logout"),
    path('customers', views.view_customers, name="view_customers"),
    path('users', views.view_users, name="view_users"),
    path('drivers', views.view_drivers, name="view_drivers"),
    path('vehicles', views.manage_vehicles, name="manage_vehicles"),
    path('vehicles-group', views.vehicles_group, name="vehicles_group"),    


    path('delinquent-report', views.delinquent_report, name="delinquent_report"),
    path('monthly-report', views.monthly_report, name="monthly_report"),
    path('booking-report', views.booking_report, name="booking_report"),
    path('users-report', views.users_report, name="users_report"),
    path('fuel-report', views.fuel_report, name="fuel_report"),
    path('driver-report', views.driver_report, name='driver_report'),
    path('customer-report', views.customer_report, name="customer_report"),
    path('vendor-report', views.vendor_report, name='vendor_report'),
    path('yearly-report', views.yearly_report, name='yearly_report'),


    path('addvendor', views.add_vendor, name='add_vendor'),
    path('manage-vendors', views.manage_vendor, name='manage_vendor'),
    path('add-workorder', views.add_workorder, name="add_workorder"),
    path('manage-workorders', views.manage_workorder, name="manage_workorder"),
    path('add-note', views.add_note , name="add_note"),
    path('manage-notes', views.manage_note, name="manage_note"),
    path('settings-general', views.general_settings, name="general_settings"),
    path('settings-api', views.api_settings, name="api_settings"),
    path('settings-reason', views.cancellation_reason, name="cancellation_reason"),
    path('settings-email-notification', views.email_notification, name="email_notification"),
    path('settings-email-content', views.email_content, name="email_content"),
    path('settings-fare', views.fare_settings, name="fare_settings"),
    path('settings-expense', views.expense_categories, name='expense_categories'),
    path('settings-income', views.income_categories, name="income_categories"), 

    path('add-vehicle', views.add_vehicle , name="add_vehicle"),
    path('edit-vehicle/<int:id>', views.edit_vehicle , name="edit_vehicle"),
    path('delete-vehicle/<int:id>', views.delete_vehicle, name="delete_vehicle"),


    path('add-vehicle-group', views.add_vehicle_group, name="add_vehicle_group"),
    path('update-vehicle-group/<int:id>', views.update_vehicle_group, name = "update_vehicle_group"),
    path('delete-vehicle-group/<int:id>', views.delete_vehicle_group, name="delete_vehicle_group"),


    path('add-workorder', views.add_workorder, name="add_workorder"),
    path('update-workorder/<int:id>', views.update_workorder, name = "update_workorder"),
    path('delete-workorder/<int:id>', views.delete_workorder, name="delete_workorder"),


    path('add-vendor', views.add_vendor, name="add_vendor"),
    path('update-vendor/<int:id>', views.update_vendor, name = "update_vendor"),
    path('delete-vendor/<int:id>', views.delete_vendor, name="delete_vendor"),


    path('add-note', views.add_note, name="add_note"),
    path('update-note/<int:id>', views.update_note, name = "update_note"),
    path('delete-note/<int:id>', views.delete_note, name="delete_note"),


    path('add-reminder', views.add_reminder, name="add_reminder"),
    path('manage-reminder', views.manage_reminder, name="manage_reminder"),
    path('update-reminder/<int:id>', views.update_reminder, name="update_reminder"),
    path('delete-reminder/<int:id>', views.delete_reminder, name="delete_reminder"),


    path('reminder-service-item', views.service_item, name="service_item"),
    path('add-service-item', views.add_service_item, name="add_service_item"),
    path('update-service-item', views.update_service_item, name="update_service_item"),
    path('delete-service-item', views.delete_service_item, name="delete_service_item"),

    path('transactions-income', views.manage_income, name="manage_income"),
    path('add-income', views.add_income, name="add_income"),
    path('delete-income/<int:id>', views.delete_income, name="delete_income"),

    path('transactions-expense', views.manage_expense, name="manage_expense"),
    path('add-expense', views.add_expense, name="add_expense"),
    path('delete-expense/<int:id>', views.delete_expense, name="delete_expense"),


 # Booking Feature URLS
    path('newbooking', views.new_booking, name="new_booking"),
    path('edit-booking/<int:id>', views.edit_booking, name="edit_booking"),
    path('delete-booking/<int:id>', views.delete_booking, name="delete_booking"),
    path('managebooking', views.manage_booking, name="manage_booking"),
    path('bookingcalendar', views.booking_calendar, name="booking_calendar"),

# Fuel Feature URLS
    path('addfuel', views.add_fuel, name="add_fuel"),
    path('fuelhistory', views.fuel_history, name='fuel_history'),
    path('update-fuel/<int:id>', views.update_fuel, name='update_fuel'),
    path('delete-fuel/<int:id>', views.delete_fuel, name='delete_fuel'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)