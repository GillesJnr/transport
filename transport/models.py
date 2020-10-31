from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models


class Addresses(models.Model):
    customer_id = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'addresses'
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return self.address


class Allocation(models.Model):
    month = models.TextField()
    amount = models.FloatField()

    class Meta:
        managed = True
        db_table = 'allocation'
        verbose_name = "Allocation"
        verbose_name_plural = "Allocations"

    def __str__(self):
        return self.month


class ApiSettings(models.Model):
    key_name = models.CharField(max_length=255, blank=True, null=True)
    key_value = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'api_settings'
        verbose_name = "Api_Setting"
        verbose_name_plural = "Api_Settings"

    def __str__(self):
        return self.key_name





class BookingIncome(models.Model):
    booking_id = models.IntegerField(blank=True, null=True)
    income_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'booking_income'
        verbose_name = "Booking Income"
        

    def __str__(self):
        return self.booking_id


class Bookings(models.Model):
    customer_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    vehicle_id = models.IntegerField(blank=True, null=True)
    driver_id = models.IntegerField(blank=True, null=True)
    pickup = models.DateTimeField(blank=True, null=True)
    dropoff = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    pickup_addr = models.CharField(max_length=255, blank=True, null=True)
    dest_addr = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    travellers = models.IntegerField()
    status = models.IntegerField()
    payment = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bookings'


class BookingsMeta(models.Model):
    booking_id = models.PositiveIntegerField()
    type = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bookings_meta'
        verbose_name = "Bookings Meta"
        verbose_name_plural = "Bookings Meta"

    def __str__(self):
        return self.key


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = True
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = True
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = True
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = True
#         db_table = 'django_session'


class DriverVehicle(models.Model):
    vehicle_id = models.IntegerField(blank=True, null=True)
    driver_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'driver_vehicle'
        verbose_name_plural = "DriverVehicles"

    def __str__(self):
        return self.vehicle_id


class EmailContent(models.Model):
    key = models.CharField(max_length=255, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'email_content'

    def __str__(self):
        return self.key


class Expense(models.Model):
    vehicle_id = models.IntegerField(blank=True, null=True)
    exp_id = models.IntegerField(blank=True, null=True)
    amount = models.FloatField()
    user_id = models.IntegerField(blank=True, null=True)
    expense_type = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'expense'

    def __str__(self):
        return self.comment


class ExpenseCat(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=5, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'expense_cat'

    def __str__(self):
        return self.type


class FareSettings(models.Model):
    key_name = models.CharField(max_length=255, blank=True, null=True)
    key_value = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fare_settings'
        verbose_name = "Fare Setting"
        verbose_name_plural = "Fare Settings"


    def __str__(self):
        return self.key_name


class Fuel(models.Model):
    vehicle_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    start_meter = models.CharField(max_length=255, blank=True, null=True)
    end_meter = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    vendor_name = models.CharField(max_length=255, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    fuel_from = models.CharField(max_length=255, blank=True, null=True)
    cost_per_unit = models.CharField(max_length=255, blank=True, null=True)
    consumption = models.IntegerField(blank=True, null=True)
    complete = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fuel'


    def __str__(self):
        return self.reference


class Income(models.Model):
    vehicle_id = models.IntegerField(blank=True, null=True)
    income_id = models.IntegerField(blank=True, null=True)
    amount = models.FloatField()
    user_id = models.IntegerField(blank=True, null=True)
    income_cat = models.IntegerField(blank=True, null=True)
    mileage = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'income'


    def __str__(self):
        return self.income_id


class IncomeCat(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=5, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'income_cat'


    def __str__(self):
        return self.name


class Maintanance(models.Model):
    service_id = models.IntegerField(blank=True, null=True)
    vehicle_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'maintanance'


class Message(models.Model):
    fcm_id = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'message'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'migrations'


class Mileage(models.Model):
    vehicle_id = models.IntegerField(blank=True, null=True)
    mileage = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mileage'


class Notes(models.Model):
    vehicle_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    submitted_on = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'notes'

    def __str__(self):
        return self.note


class Notifications(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    type = models.CharField(max_length=255)
    notifiable_type = models.CharField(max_length=255)
    notifiable_id = models.BigIntegerField()
    data = models.TextField()
    read_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'notifications'
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"


    def __str__(self):
        return self.id


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'password_resets'


class Reasons(models.Model):
    reason = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'reasons'
        verbose_name = "Reason"
        verbose_name_plural = "Reasons"

    def __str__(self):
        return self.reason


class Reviews(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    booking_id = models.IntegerField(blank=True, null=True)
    driver_id = models.IntegerField(blank=True, null=True)
    ratings = models.FloatField(blank=True, null=True)
    review_text = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'reviews'
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return self.review_text


class ServiceItems(models.Model):
    description = models.TextField(blank=True, null=True)
    time_interval = models.CharField(max_length=255, blank=True, null=True)
    overdue_time = models.CharField(max_length=255, blank=True, null=True)
    overdue_unit = models.CharField(max_length=255, blank=True, null=True)
    meter_interval = models.CharField(max_length=255, blank=True, null=True)
    overdue_meter = models.CharField(max_length=255, blank=True, null=True)
    show_time = models.CharField(max_length=255, blank=True, null=True)
    duesoon_time = models.CharField(max_length=255, blank=True, null=True)
    duesoon_unit = models.CharField(max_length=255, blank=True, null=True)
    show_meter = models.CharField(max_length=255, blank=True, null=True)
    duesoon_meter = models.CharField(max_length=255, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'service_items'
        verbose_name = "Service Item"
        verbose_name_plural = "Service Items"

    def __str__(self):
        return self.description


class ServiceReminder(models.Model):
    vehicle_id = models.IntegerField(blank=True, null=True)
    service_id = models.IntegerField(blank=True, null=True)
    last_date = models.CharField(max_length=255, blank=True, null=True)
    last_meter = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'service_reminder'


class Settings(models.Model):
    label = models.CharField(max_length=255)
    name = models.CharField(unique=True, max_length=255)
    value = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'settings'


class Users(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    user_type = models.CharField(max_length=255, blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    api_token = models.CharField(unique=True, max_length=60)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default= timezone.now, blank=True, null=True)
    updated_at = models.DateTimeField(default= timezone.now, blank=True, null=True)
    deleted_at = models.DateTimeField(default= timezone.now, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'users'
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name


class UsersMeta(models.Model):
    user_id = models.PositiveIntegerField()
    type = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'users_meta'

    def __str__(self):
        return self.key


class VehicleGroup(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vehicle_group'

    def __str__(self):
        return self.name


class Vehicles(models.Model):
    make = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    lic_exp_date = models.DateField(blank=True, null=True)
    reg_exp_date = models.DateField(blank=True, null=True)
    vehicle_image = models.CharField(max_length=255, blank=True, null=True)
    engine_type = models.CharField(max_length=255, blank=True, null=True)
    horse_power = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    vin = models.CharField(max_length=255, blank=True, null=True)
    license_plate = models.CharField(max_length=255)
    mileage = models.IntegerField(blank=True, null=True)
    in_service = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    int_mileage = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vehicles'
        verbose_name = "Vehicle"

    def __str__(self):
        return self.make


class VehiclesMeta(models.Model):
    vehicle_id = models.PositiveIntegerField()
    type = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vehicles_meta'

    def __str__(self):
        return self.key

class Vendors(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    custom_type = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vendors'
        verbose_name = "Vendor"

    def __str__(self):
        return self.name


class WorkOrders(models.Model):
    created_on = models.DateField(blank=True, null=True)
    required_by = models.DateField(blank=True, null=True)
    vehicle_id = models.IntegerField(blank=True, null=True)
    vendor_id = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    meter = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'work_orders'
