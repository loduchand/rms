# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class BuildJobInfo(models.Model):
    build_id = models.AutoField(primary_key=True)
    job = models.CharField(max_length=1000, blank=True, null=True)
    build_no = models.IntegerField(blank=True, null=True)
    branch_name = models.CharField(max_length=1000, blank=True, null=True)
    build_id_jenkins = models.TextField(blank=True, null=True)
    build_tags = models.TextField(blank=True, null=True)
    product_name = models.TextField(blank=True, null=True)
    version = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    arch = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1000, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    zip_location = models.TextField(blank=True, null=True)
    rpm_location = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'build_job_info'


class BuildRequest(models.Model):
    product_name = models.CharField(max_length=1000, blank=True, null=True)
    version = models.CharField(max_length=1000, blank=True, null=True)
    release = models.CharField(max_length=1000, blank=True, null=True)
    platform_os_id = models.IntegerField(blank=True, null=True)
    platform_ws_id = models.IntegerField(blank=True, null=True)
    product_arch_id = models.IntegerField(blank=True, null=True)
    output_directory = models.CharField(max_length=1000, blank=True, null=True)
    input_type_id = models.CharField(max_length=1000, blank=True, null=True)
    build_type_id = models.CharField(max_length=1000, blank=True, null=True)
    batch_id = models.CharField(max_length=1000, blank=True, null=True)
    platform_spec_id = models.IntegerField(blank=True, null=True)
    build_status = models.CharField(max_length=1000, blank=True, null=True)
    request_time = models.DateTimeField(blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=1000)
    file = models.CharField(max_length=1000, blank=True, null=True)
    comments = models.CharField(max_length=1000, blank=True, null=True)
    release_notes_url = models.CharField(max_length=1000, blank=True, null=True)
    release_notes = models.CharField(max_length=1000)
    derived_build_id = models.IntegerField(blank=True, null=True)
    build_id = models.IntegerField(blank=True, null=True)
    job_name = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'build_request'


class BuildType(models.Model):
    build_type_id = models.CharField(primary_key=True, max_length=1000)
    build_type_name = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'build_type'


class InputType(models.Model):
    input_type_id = models.CharField(primary_key=True, max_length=1000)
    input_type_name = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'input_type'


class PlatformArch(models.Model):
    arch_id = models.AutoField(primary_key=True)
    arch_name = models.CharField(unique=True, max_length=1000, blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'platform_arch'


class PlatformJre(models.Model):
    jre_id = models.AutoField(primary_key=True)
    jre_name = models.CharField(unique=True, max_length=1000, blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'platform_jre'


class PlatformOs(models.Model):
    os_id = models.AutoField(primary_key=True)
    os_name = models.CharField(unique=True, max_length=1000, blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'platform_os'


class PlatformSpecIdvsproductName(models.Model):
    platform_spec_id = models.CharField(max_length=1000, blank=True, null=True)
    product_name = models.CharField(max_length=1000, blank=True, null=True)
    date_added = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'platform_spec_idvsproduct_name'


class PlatformSpecVersion(models.Model):
    product_platform_spec_id = models.IntegerField(blank=True, null=True)
    version_a = models.CharField(max_length=1000, blank=True, null=True)
    version_b = models.CharField(max_length=1000, blank=True, null=True)
    version_c = models.CharField(max_length=1000, blank=True, null=True)
    version_d = models.CharField(max_length=1000, blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    derived_build_id = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'platform_spec_version'


class PlatformWs(models.Model):
    ws_id = models.AutoField(primary_key=True)
    ws_name = models.CharField(unique=True, max_length=1000, blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'platform_ws'


class ReleaseNotes(models.Model):
    location = models.CharField(max_length=1000, blank=True, null=True)
    filename = models.CharField(max_length=1000, blank=True, null=True)
    branch = models.CharField(max_length=10, blank=True, null=True)
    release = models.CharField(max_length=1000, blank=True, null=True)
    fixes = models.TextField(blank=True, null=True)
    features = models.TextField(blank=True, null=True)
    impact_area = models.TextField(blank=True, null=True)
    test_cases = models.TextField(blank=True, null=True)
    synchronisation_status = models.CharField(max_length=1000, blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    batch_id = models.CharField(max_length=1000, blank=True, null=True)
    platform_spec_id = models.IntegerField(blank=True, null=True)
    build_version = models.CharField(max_length=1000, blank=True, null=True)
    product_name = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'release_notes'


class RpmMakeInfo(models.Model):
    tag = models.CharField(max_length=1000, blank=True, null=True)
    module = models.CharField(max_length=1000, blank=True, null=True)
    version = models.CharField(max_length=1000, blank=True, null=True)
    user_id = models.CharField(max_length=1000, blank=True, null=True)
    release = models.CharField(max_length=1000, blank=True, null=True)
    base = models.CharField(max_length=1000, blank=True, null=True)
    base_command = models.CharField(max_length=1000, blank=True, null=True)
    revision_command = models.CharField(max_length=1000, blank=True, null=True)
    file = models.CharField(max_length=1000, blank=True, null=True)
    md5 = models.CharField(max_length=1000, blank=True, null=True)
    dir = models.CharField(max_length=1000, blank=True, null=True)
    mode = models.CharField(max_length=1000, blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rpm_make_info'