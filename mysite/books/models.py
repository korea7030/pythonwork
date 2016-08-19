# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
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
    action_flag = models.SmallIntegerField()
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


class TbBook(models.Model):
    c_seq = models.AutoField(db_column='C_SEQ', primary_key=True)  # Field name made lowercase.
    c_bno = models.CharField(db_column='C_bNO', max_length=5, blank=True, null=True)  # Field name made lowercase.
    c_ttle = models.CharField(db_column='C_TTLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    c_sbttle = models.CharField(db_column='C_SBTTLE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    c_authr = models.CharField(db_column='C_AUTHR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    c_publshr = models.CharField(db_column='C_PUBLSHR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    c_pub_dt = models.DateField(db_column='C_PUB_DT', blank=True, null=True)  # Field name made lowercase.
    c_formt = models.CharField(db_column='C_FORMT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    c_pges = models.IntegerField(db_column='C_PGES', blank=True, null=True)  # Field name made lowercase.
    c_sttus = models.CharField(db_column='C_STTUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    c_rting = models.IntegerField(db_column='C_RTING', blank=True, null=True)  # Field name made lowercase.
    c_ys24rt = models.IntegerField(db_column='C_YS24RT', blank=True, null=True)  # Field name made lowercase.
    c_diffrting = models.IntegerField(db_column='C_DIFFRTING', blank=True, null=True)  # Field name made lowercase.
    c_categry = models.CharField(db_column='C_CATEGRY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    c_strt_dt = models.DateField(db_column='C_STRT_DT', blank=True, null=True)  # Field name made lowercase.
    c_fin_dt = models.DateField(db_column='C_FIN_DT', blank=True, null=True)  # Field name made lowercase.
    c_red_prid = models.IntegerField(db_column='C_RED_PRID', blank=True, null=True)  # Field name made lowercase.
    c_week_yn = models.CharField(db_column='C_WEEK_YN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    c_red_tm = models.IntegerField(db_column='C_RED_TM', blank=True, null=True)  # Field name made lowercase.
    c_red_resn = models.CharField(db_column='C_RED_RESN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    c_fund_rou = models.CharField(db_column='C_FUND_ROU', max_length=30, blank=True, null=True)  # Field name made lowercase.
    c_rou_cat = models.CharField(db_column='C_ROU_CAT', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_book'


class TbBookTime(models.Model):
    c_seq = models.AutoField(db_column='C_SEQ', primary_key=True)  # Field name made lowercase.
    c_bno = models.CharField(db_column='C_bNO', max_length=5, blank=True, null=True)  # Field name made lowercase.
    c_strt_tm = models.DateTimeField(db_column='C_STRT_TM', blank=True, null=True)  # Field name made lowercase.
    c_fin_tm = models.DateTimeField(db_column='C_FIN_TM', blank=True, null=True)  # Field name made lowercase.
    c_red_plc = models.CharField(db_column='C_RED_PLC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    c_mv_plc = models.CharField(db_column='C_MV_PLC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    c_nred_resn = models.CharField(db_column='C_NRED_RESN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    c_week_yn = models.CharField(db_column='C_WEEK_YN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    c_strt_pg_nm = models.IntegerField(db_column='C_STRT_PG_NM', blank=True, null=True)  # Field name made lowercase.
    c_fin_pg_nm = models.IntegerField(db_column='C_FIN_PG_NM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_book_time'
