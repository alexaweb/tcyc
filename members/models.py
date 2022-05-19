# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'




class Membership(models.Model):
    memb_person_id = models.IntegerField(primary_key=True)
    memb_apoderado1_id = models.IntegerField(blank=True, null=True)
    memb_apoderado2_id = models.IntegerField(blank=True, null=True)
    memb_product_id = models.IntegerField(blank=True, null=True)
    memb_season = models.IntegerField(blank=True, null=True)
    mem_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'membership'


class Order(models.Model):
    index = models.IntegerField(db_column='index')
    num_pedido = models.IntegerField(db_column='order_number', primary_key=True,verbose_name="pedido")  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    fecha = models.DateTimeField(db_column='order_date', blank=True, null=True,verbose_name="fecha")  # Field name made lowercase.
    cliente = models.TextField(db_column='order_user', blank=True, null=True,verbose_name="usuario")  # Field name made lowercase.
    email = models.TextField(db_column='order_email', blank=True, null=True)  # Field name made lowercase.
    estado = models.TextField(db_column='order_state', blank=True, null=True)  # Field name made lowercase.
    forma_de_pago = models.TextField(db_column='order_paymentmethod', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    promotion_id = models.TextField(db_column='order_promotion',blank=True, null=True)
    total = models.FloatField(db_column='order_total', blank=True, null=True)  # Field name made lowercase.
    total_pagado = models.FloatField(db_column='order_total_paid', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    order_items = models.TextField(db_column='order_items',blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'orders'
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

#comment

class Form(models.Model):
    index = models.IntegerField(db_column='index',primary_key=True)
    productos_field = models.TextField(db_column='Producto(s)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
    apellido_paterno = models.TextField(db_column='Apellido Paterno', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    apellido_materno = models.TextField(db_column='Apellido Materno', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    correo = models.TextField(db_column='Correo', blank=True, null=True)  # Field name made lowercase.
    rut = models.TextField(db_column='RUT', blank=True, null=True)  # Field name made lowercase.
    #num_pedido = models.IntegerField(db_column='Número de pedido', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    order = models.ForeignKey(Order,on_delete=models.DO_NOTHING,db_column='Número de pedido',related_name='num_pedidoOf')
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'forms'

class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    person_rut = models.CharField(max_length=15, blank=True, null=True)
    person_fechanac = models.DateField(blank=True, null=True)
    person_apaterno = models.CharField(max_length=30)
    person_amaterno = models.CharField(max_length=30, blank=True, null=True)
    person_nombres = models.CharField(max_length=30)
    person_email = models.CharField(max_length=50, blank=True, null=True)
    person_telefono = models.CharField(max_length=20, blank=True, null=True)
    person_apoderado_1 = models.IntegerField(blank=True, null=True)
    person_apoderado_2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'


class PersonUser(models.Model):
    person_id = models.IntegerField()
    user_email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'person_user'
        unique_together = (('person_id', 'user_email'),)


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=25, blank=True, null=True)
    product_description = models.CharField(max_length=50, blank=True, null=True)
    product_category = models.IntegerField(blank=True, null=True)
    product_key = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class Test(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    field_field = models.FloatField(db_column='#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    fecha = models.TextField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    cliente = models.TextField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    forma_de_pago = models.TextField(db_column='Forma de Pago', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    promotion_id = models.TextField(blank=True, null=True)
    total = models.TextField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    total_pagado = models.TextField(db_column='Total pagado', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    order_items = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'
