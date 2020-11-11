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
    path('transactions/income', views.manage_income, name="manage_income"),
    path('transactions/expense', views.manage_expense, name="manage_expense"),
    path('bookings/newbooking', views.new_booking, name="new_booking"),
    path('bookings/managebooking', views.manage_booking, name="manage_booking"),
    path('bookings/bookingcalendar', views.booking_calendar, name="booking_calendar"),
    path('reports/delinquent', views.delinquent_report, name="delinquent_report"),
    path('reports/monthly', views.monthly_report, name="monthly_report"),
    path('reports/booking', views.booking_report, name="booking_report"),
    path('reports/users', views.users_report, name="users_report"),
    path('reports/fuel', views.fuel_report, name="fuel_report"),
    path('reports/driver', views.driver_report, name='driver_report'),
    path('reports/customer', views.customer_report, name="customer_report"),
    path('reports/vendor', views.vendor_report, name='vendor_report'),
    path('reports/yearly', views.yearly_report, name='yearly_report'),
    path('fuel/addfuel', views.add_fuel, name="add_fuel"),
    path('fuel/fuelhistory', views.fuel_history, name='fuel_history'),
    path('vendors/add', views.add_vendor, name='add_vendor'),
    path('vendors/manage', views.manage_vendor, name='manage_vendor'),
    path('workorder/add', views.add_workorder, name="add_workorder"),
    path('workorder/manage', views.manage_workorder, name="manage_workorder"),
    path('notes/add', views.add_note , name="add_note"),
    path('notes/manage', views.manage_note, name="manage_note"),
    path('reminder/add', views.add_reminder, name="add_reminder"),
    path('reminder/manage', views.manage_reminder, name="manage_reminder"),
    path('reminder/service-item', views.service_item, name="service_item"),
    path('settings/general', views.general_settings, name="general_settings"),
    path('settings/api', views.api_settings, name="api_settings"),
    path('settings/reason', views.cancellation_reason, name="cancellation_reason"),
    path('settings/email-notification', views.email_notification, name="email_notification"),
    path('settings/email-content', views.email_content, name="email_content"),
    path('settings/fare', views.fare_settings, name="fare_settings"),
    path('settings/expense', views.expense_categories, name='expense_categories'),
    path('settings/income', views.income_categories, name="income_categories"), 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)