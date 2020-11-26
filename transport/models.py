from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Q
# from datetime import timedelta
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from django.contrib.auth.models import UserManager, AbstractUser

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models


class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    user_image = models.ImageField(blank=True, null=True)
    #password = models.CharField(max_length=255, blank=True, null=True)
    user_type = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    api_token = models.CharField(unique=True, max_length=60,blank=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default= timezone.now, blank=True, null=True)
    updated_at = models.DateTimeField(default= timezone.now, blank=True, null=True)
    deleted_at = models.DateTimeField(default= timezone.now, blank=True, null=True)


    # is_active = models.NullBooleanField(default=True, null=True)
    # is_staff = models.NullBooleanField(default=False, null=True)
    # is_anonymous = models.NullBooleanField(default=False, null = True)
    # is_authenticated = models.NullBooleanField(default=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()


    class Meta:
        managed = True
        db_table = 'users'
        verbose_name = "User"
        verbose_name_plural = "Users"
        #   swappable = 'AUTH_USER_MODEL'
    

    

    def __str__(self):
        return self.name

class Addresses(models.Model):
    addresses_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses", null=True)
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
    allocation_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="allocation", null=True)
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
    apisettings_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="apisettings", null=True)
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
    bookingincome_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookingincomes", null=True)
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
        return str(self.bookingincome_user)


class Bookings(models.Model):
    bookings_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings", null=True)
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


    def __str__(self):
        return str(self.bookings_user)


class BookingsMeta(models.Model):
    bookingsmeta_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookingsmeta", null=True)
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
    drivervehicle_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="drivervehicles", null=True)
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
    emailcontent_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="emailcontents", null=True)
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
    expense_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expenses", null=True)
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
    expensecat_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expensecats", null=True)
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
    # faresettings_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="faresettings", null=True)
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
    fuel_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="fuels", null=True)
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
        return str (self.reference)


class Income(models.Model):
    income_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="incomes", null=True)
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
        return str (self.income_user)


class IncomeCat(models.Model):
    incomecat_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="incomecats", null=True)
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
    maintenance_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="maintanance", null=True)
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
    message_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages", null=True)
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
    migrations_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="migrations", null=True)
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'migrations'


class Mileage(models.Model):
    mileage_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mileages", null=True)
    vehicle_id = models.IntegerField(blank=True, null=True)
    mileage = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mileage'

    def __str__(self):
        return str(self.mileage_user)




class Notifications(models.Model):
    notifications_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications", null=True)
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
        return self.notifiable_type

class PasswordResets(models.Model):
    passwordresets_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="passwordresets", null=True)
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'password_resets'


class Reasons(models.Model):
    reasons_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reasons", null=True)
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
    reviews_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews", null=True)
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
    # serviceitem_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="serviceitems", null=True)
    description = models.TextField(blank=True, null=True)
    time_interval = models.CharField(max_length=255, blank=True, null=True)
    overdue_time = models.IntegerField(blank=True, null=True)
    overdue_unit = models.CharField(max_length=255, blank=True, null=True)
    meter_interval = models.CharField(max_length=255, blank=True, null=True)
    overdue_meter = models.IntegerField(blank=True, null=True)
    show_time = models.CharField(max_length=255, blank=True, null=True)
    duesoon_time = models.IntegerField(blank=True, null=True)
    duesoon_unit = models.CharField(max_length=255, blank=True, null=True)
    show_meter = models.CharField(max_length=255, blank=True, null=True)
    duesoon_meter = models.IntegerField(blank=True, null=True)
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




class Settings(models.Model):
    settings_user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="settings", null=True)
    label = models.CharField(max_length=255)
    name = models.CharField(unique=True, max_length=255)
    value = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'settings'

    def __str__(self):
        return self.settings_user




class UsersMeta(models.Model):
    usersmeta_user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="usersmeta", null=True)
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
    # vehiclegroup_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vehiclegroup", null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now = True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vehicle_group'

    def __str__(self):
        return self.name

class EngineType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Vehicles(models.Model):
    vehicles_user = models.ForeignKey(Users , on_delete=models.CASCADE, related_name="vehicles", null=True)
    make = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    group = models.ForeignKey(VehicleGroup, on_delete=models.CASCADE, related_name="vehicle_group", null=True)
    lic_exp_date = models.DateField(blank=True, null=True)
    reg_exp_date = models.DateField(blank=True, null=True)
    vehicle_image = models.ImageField(blank=True, null=True)
    engine_type = models.ForeignKey(EngineType, on_delete=models.CASCADE, null=True)
    horse_power = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    vin = models.CharField(max_length=255, blank=True, null=True)
    license_plate = models.CharField(max_length=255)
    mileage = models.IntegerField(blank=True, null=True)
    in_service = models.BooleanField(blank=True, null=True)
    # user_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True ,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    initial_mileage = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vehicles'
        verbose_name = "Vehicle"

    def __str__(self):
        return self.make


class VehiclesMeta(models.Model):
    vehiclesmeta_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vehiclesmeta", null=True)
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


class VendorType(models.Model):
    type = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.type


class Vendors(models.Model):
    # vendors_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vendors", null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)
    type = models.ForeignKey(VendorType, on_delete=models.CASCADE, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    # custom_type = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    deleted_at = models.DateTimeField(auto_now = True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now = True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vendors'
        verbose_name = "Vendor"

    def __str__(self):
        return self.name


class WorkOrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name



class WorkOrders(models.Model):
    # workorder_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workorders", null=True)
    created_on = models.DateField(blank=True, null=True)
    required_by = models.DateField(blank=True, null=True)
    wo_vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE, blank=True, null=True)
    wo_vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    status = models.ForeignKey(WorkOrderStatus, on_delete=models.CASCADE)
    description = models.CharField(max_length=400, blank=True, null=True)
    meter = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'work_orders'
        verbose_name = "Work Order"
        verbose_name_plural = 'Work Orders'


class Notes(models.Model):
    note_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes", null=True)
    note_vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE, related_name="vehicles", blank=True, null=True)
    note_customer = models.IntegerField(blank=True, null=True)
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


class ServiceReminder(models.Model):
    # servicereminder_user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="servicereminders", null=True)
    sr_vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE, related_name="vehicleservice" ,blank=True, null=True)
    sr_service = models.ForeignKey(ServiceItems, on_delete=models.CASCADE, related_name="service",blank=True, null=True)
    last_date = models.DateField(blank=True, null=True)
    last_meter = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'service_reminder'

    def __str__(self):
        return str(self.sr_vehicle)