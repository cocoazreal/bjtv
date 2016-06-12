# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Action(models.Model):
    keyid = models.CharField(primary_key=True, max_length=255)
    idaction = models.CharField(max_length=255, blank=True, null=True)
    idsite = models.CharField(max_length=255, blank=True, null=True)
    idvisit = models.CharField(max_length=255, blank=True, null=True)
    idvisitor = models.CharField(max_length=255, blank=True, null=True)
    atype = models.CharField(max_length=255, blank=True, null=True)
    itype = models.CharField(max_length=255, blank=True, null=True)
    tpdata = models.CharField(max_length=1024, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=1024, blank=True, null=True)
    evtid = models.CharField(max_length=255, blank=True, null=True)
    evtlabel = models.CharField(db_column='evtLabel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    field_date = models.BigIntegerField(db_column='_date', blank=True, null=True)  # Field renamed because it started with '_'.
    version = models.CharField(max_length=255, blank=True, null=True)
    channel = models.CharField(max_length=255, blank=True, null=True)
    field_user = models.CharField(db_column='_user', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    age = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    proin = models.CharField(max_length=255, blank=True, null=True)
    ts = models.CharField(max_length=255, blank=True, null=True)
    cy = models.CharField(max_length=255, blank=True, null=True)
    pro = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    ref_url = models.CharField(max_length=1024, blank=True, null=True)
    ivr = models.CharField(max_length=255, blank=True, null=True)
    lcltime = models.CharField(max_length=255, blank=True, null=True)
    bsn = models.CharField(max_length=255, blank=True, null=True)
    bsv = models.CharField(max_length=255, blank=True, null=True)
    cookie = models.CharField(max_length=255, blank=True, null=True)
    director = models.CharField(max_length=255, blank=True, null=True)
    flash = models.CharField(max_length=255, blank=True, null=True)
    gears = models.CharField(max_length=255, blank=True, null=True)
    field_java = models.CharField(db_column='_java', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    os = models.CharField(max_length=255, blank=True, null=True)
    pdf = models.CharField(max_length=255, blank=True, null=True)
    qkt = models.CharField(max_length=255, blank=True, null=True)
    rpr = models.CharField(max_length=255, blank=True, null=True)
    res = models.CharField(max_length=255, blank=True, null=True)
    silt = models.CharField(max_length=255, blank=True, null=True)
    winml = models.CharField(max_length=255, blank=True, null=True)
    bizd = models.CharField(max_length=1024, blank=True, null=True)


class Statistics(models.Model):
    keyid = models.CharField(max_length=255)
    destid = models.CharField(max_length=255)
    idvisit = models.CharField(max_length=255, blank=True, null=True)
    idaction = models.CharField(max_length=255, blank=True, null=True)
    idvisitor = models.CharField(max_length=255, blank=True, null=True)
    field_date = models.BigIntegerField(db_column='_date', blank=True, null=True)  # Field renamed because it started with '_'.
    field_key = models.CharField(db_column='_key', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    field_value = models.CharField(db_column='_value', max_length=1024, blank=True, null=True)  # Field renamed because it started with '_'.


class Visit(models.Model):
    keyid = models.CharField(primary_key=True, max_length=255)
    idsite = models.CharField(max_length=255, blank=True, null=True)
    idvisit = models.CharField(max_length=255, blank=True, null=True)
    idvisitor = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    channel = models.CharField(max_length=255, blank=True, null=True)
    field_user = models.CharField(db_column='_user', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    age = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    proin = models.CharField(max_length=255, blank=True, null=True)
    mbr = models.CharField(max_length=255, blank=True, null=True)
    entry_name = models.CharField(max_length=255, blank=True, null=True)
    entry_url = models.CharField(max_length=1024, blank=True, null=True)
    exit_name = models.CharField(max_length=255, blank=True, null=True)
    exit_url = models.CharField(max_length=1024, blank=True, null=True)
    entry_time = models.BigIntegerField(blank=True, null=True)
    exit_time = models.BigIntegerField(blank=True, null=True)
    cy = models.CharField(max_length=255, blank=True, null=True)
    pro = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    ref_url = models.CharField(max_length=1024, blank=True, null=True)
    ts = models.CharField(max_length=255, blank=True, null=True)
    pages = models.CharField(max_length=255, blank=True, null=True)
    ivr = models.CharField(max_length=255, blank=True, null=True)
    vlt = models.CharField(max_length=255, blank=True, null=True)
    bsn = models.CharField(max_length=255, blank=True, null=True)
    bsv = models.CharField(max_length=255, blank=True, null=True)
    cookie = models.CharField(max_length=255, blank=True, null=True)
    director = models.CharField(max_length=255, blank=True, null=True)
    flash = models.CharField(max_length=255, blank=True, null=True)
    gears = models.CharField(max_length=255, blank=True, null=True)
    field_java = models.CharField(db_column='_java', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    os = models.CharField(max_length=255, blank=True, null=True)
    pdf = models.CharField(max_length=255, blank=True, null=True)
    qkt = models.CharField(max_length=255, blank=True, null=True)
    rpr = models.CharField(max_length=255, blank=True, null=True)
    res = models.CharField(max_length=255, blank=True, null=True)
    silt = models.CharField(max_length=255, blank=True, null=True)
    winml = models.CharField(max_length=255, blank=True, null=True)
    bsl = models.CharField(max_length=255, blank=True, null=True)
    bsc = models.CharField(max_length=255, blank=True, null=True)
    visit_deep_actions = models.CharField(max_length=255, blank=True, null=True)

