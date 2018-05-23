# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Characteristics(models.Model):
    product = models.ForeignKey('Product', models.DO_NOTHING, primary_key=True)
    property = models.ForeignKey('Property', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'characteristics'
        unique_together = (('product', 'property'),)


class Clients(models.Model):
    clients_id = models.AutoField(primary_key=True)
    address = models.TextField(blank=True, null=True)  # This field type is a guess.
    fullname = models.TextField(blank=True, null=True)  # This field type is a guess.
    telno = models.CharField(max_length=15, blank=True, null=True)
    login = models.CharField(max_length=15, blank=True, null=True)
    userpass = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients'


class Log(models.Model):
    operation_time = models.DateTimeField(blank=True, null=True)
    user_id = models.TextField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    event_descr = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log'


class Orders(models.Model):
    orders_id = models.AutoField(primary_key=True)
    clients = models.ForeignKey(Clients, models.DO_NOTHING, blank=True, null=True)
    date_finish = models.DateField(blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    orders_date = models.DateField(blank=True, null=True)
    paid = models.NullBooleanField()
    price = models.TextField(blank=True, null=True)  # This field type is a guess.
    staff = models.ForeignKey('Staff', models.DO_NOTHING, blank=True, null=True)
    status_work = models.NullBooleanField()
    text = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)


    class Meta:
        # managed = False
        db_table = 'orders'


class Position(models.Model):
    position_id = models.AutoField(primary_key=True)
    salary = models.TextField(blank=True, null=True)  # This field type is a guess.
    title = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'position'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    orders = models.ForeignKey(Orders, models.DO_NOTHING, blank=True, null=True)
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'
        ordering = ['product_id']



class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    value = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'property'


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    address = models.TextField(blank=True, null=True)  # This field type is a guess.
    age = models.IntegerField(null=False, default=1)
    fullname = models.TextField(blank=True, null=True)  # This field type is a guess.
    position = models.ForeignKey(Position, models.DO_NOTHING, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    telno = models.CharField(max_length=15, blank=True, null=True)
    login = models.CharField(max_length=15, blank=True, null=True)
    userpass = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier'
