# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AChartdurations(models.Model):
    subject_id = models.TextField()  # This field type is a guess.
    icustay_id = models.TextField(blank=True)  # This field type is a guess.
    itemid = models.TextField()  # This field type is a guess.
    elemid = models.TextField()  # This field type is a guess.
    starttime = models.DateTimeField()
    startrealtime = models.DateTimeField()
    endtime = models.DateTimeField(blank=True, null=True)
    cuid = models.TextField(blank=True)  # This field type is a guess.
    duration = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'a_chartdurations'


class AIodurations(models.Model):
    subject_id = models.TextField()  # This field type is a guess.
    icustay_id = models.TextField(blank=True)  # This field type is a guess.
    itemid = models.TextField()  # This field type is a guess.
    elemid = models.TextField()  # This field type is a guess.
    starttime = models.DateTimeField()
    startrealtime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    cuid = models.TextField(blank=True)  # This field type is a guess.
    duration = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'a_iodurations'


class AMeddurations(models.Model):
    subject_id = models.TextField()  # This field type is a guess.
    icustay_id = models.TextField(blank=True)  # This field type is a guess.
    itemid = models.TextField()  # This field type is a guess.
    elemid = models.TextField()  # This field type is a guess.
    starttime = models.DateTimeField()
    startrealtime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    cuid = models.TextField(blank=True)  # This field type is a guess.
    duration = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'a_meddurations'


class Additives(models.Model):
    subject_id = models.TextField()  # This field type is a guess.
    icustay_id = models.TextField(blank=True)  # This field type is a guess.
    itemid = models.TextField()  # This field type is a guess.
    ioitemid = models.TextField()  # This field type is a guess.
    charttime = models.DateTimeField()
    elemid = models.TextField()  # This field type is a guess.
    cgid = models.TextField(blank=True)  # This field type is a guess.
    cuid = models.TextField(blank=True)  # This field type is a guess.
    amount = models.TextField(blank=True)  # This field type is a guess.
    doseunits = models.CharField(max_length=20, blank=True)
    route = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'additives'


class Admissions(models.Model):
    hadm_id = models.TextField(primary_key=True)  # This field type is a guess.
    subject_id = models.TextField()  # This field type is a guess.
    admit_dt = models.DateTimeField()
    disch_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'admissions'


class Censusevents(models.Model):
    census_id = models.TextField(primary_key=True)  # This field type is a guess.
    subject_id = models.TextField()  # This field type is a guess.
    intime = models.DateTimeField()
    outtime = models.DateTimeField()
    careunit = models.TextField(blank=True)  # This field type is a guess.
    destcareunit = models.TextField(blank=True)  # This field type is a guess.
    dischstatus = models.CharField(max_length=20, blank=True)
    los = models.TextField(blank=True)  # This field type is a guess.
    icustay_id = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'censusevents'


class Chartevents(models.Model):
    subject_id = models.TextField()  # This field type is a guess.
    icustay_id = models.TextField(blank=True)  # This field type is a guess.
    itemid = models.TextField()  # This field type is a guess.
    charttime = models.DateTimeField()
    elemid = models.TextField()  # This field type is a guess.
    realtime = models.DateTimeField()
    cgid = models.TextField(blank=True)  # This field type is a guess.
    cuid = models.TextField(blank=True)  # This field type is a guess.
    value1 = models.CharField(max_length=110, blank=True)
    value1num = models.TextField(blank=True)  # This field type is a guess.
    value1uom = models.CharField(max_length=20, blank=True)
    value2 = models.CharField(max_length=110, blank=True)
    value2num = models.TextField(blank=True)  # This field type is a guess.
    value2uom = models.CharField(max_length=20, blank=True)
    resultstatus = models.CharField(max_length=20, blank=True)
    stopped = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'chartevents'


class ComorbidityScores(models.Model):
    subject_id = models.TextField()  # This field type is a guess.
    hadm_id = models.TextField()  # This field type is a guess.
    category = models.CharField(max_length=10, blank=True)
    congestive_heart_failure = models.TextField(blank=True)  # This field type is a guess.
    cardiac_arrhythmias = models.TextField(blank=True)  # This field type is a guess.
    valvular_disease = models.TextField(blank=True)  # This field type is a guess.
    pulmonary_circulation = models.TextField(blank=True)  # This field type is a guess.
    peripheral_vascular = models.TextField(blank=True)  # This field type is a guess.
    hypertension = models.TextField(blank=True)  # This field type is a guess.
    paralysis = models.TextField(blank=True)  # This field type is a guess.
    other_neurological = models.TextField(blank=True)  # This field type is a guess.
    chronic_pulmonary = models.TextField(blank=True)  # This field type is a guess.
    diabetes_uncomplicated = models.TextField(blank=True)  # This field type is a guess.
    diabetes_complicated = models.TextField(blank=True)  # This field type is a guess.
    hypothyroidism = models.TextField(blank=True)  # This field type is a guess.
    renal_failure = models.TextField(blank=True)  # This field type is a guess.
    liver_disease = models.TextField(blank=True)  # This field type is a guess.
    peptic_ulcer = models.TextField(blank=True)  # This field type is a guess.
    aids = models.TextField(blank=True)  # This field type is a guess.
    lymphoma = models.TextField(blank=True)  # This field type is a guess.
    metastatic_cancer = models.TextField(blank=True)  # This field type is a guess.
    solid_tumor = models.TextField(blank=True)  # This field type is a guess.
    rheumatoid_arthritis = models.TextField(blank=True)  # This field type is a guess.
    coagulopathy = models.TextField(blank=True)  # This field type is a guess.
    obesity = models.TextField(blank=True)  # This field type is a guess.
    weight_loss = models.TextField(blank=True)  # This field type is a guess.
    fluid_electrolyte = models.TextField(blank=True)  # This field type is a guess.
    blood_loss_anemia = models.TextField(blank=True)  # This field type is a guess.
    deficiency_anemias = models.TextField(blank=True)  # This field type is a guess.
    alcohol_abuse = models.TextField(blank=True)  # This field type is a guess.
    drug_abuse = models.TextField(blank=True)  # This field type is a guess.
    psychoses = models.TextField(blank=True)  # This field type is a guess.
    depression = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'comorbidity_scores'


class DCaregivers(models.Model):
    cgid = models.TextField(primary_key=True)  # This field type is a guess.
    label = models.CharField(max_length=6, blank=True)

    class Meta:
        managed = False
        db_table = 'd_caregivers'


class DCareunits(models.Model):
    cuid = models.TextField(primary_key=True)  # This field type is a guess.
    label = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'd_careunits'


class DChartitems(models.Model):
    itemid = models.TextField(primary_key=True)  # This field type is a guess.
    label = models.CharField(max_length=110, blank=True)
    category = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'd_chartitems'


class DChartitemsDetail(models.Model):
    label = models.CharField(max_length=110, blank=True)
    label_lower = models.CharField(max_length=110, blank=True)
    itemid = models.TextField(blank=True)  # This field type is a guess.
    category = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=255, blank=True)
    value_type = models.CharField(max_length=1, blank=True)
    value_column = models.CharField(max_length=6, blank=True)
    rows_num = models.TextField(blank=True)  # This field type is a guess.
    subjects_num = models.TextField(blank=True)  # This field type is a guess.
    chart_vs_realtime_delay_mean = models.TextField(blank=True)  # This field type is a guess.
    chart_vs_realtime_delay_stddev = models.TextField(blank=True)  # This field type is a guess.
    value1_uom_num = models.TextField(blank=True)  # This field type is a guess.
    value1_uom_has_nulls = models.CharField(max_length=1, blank=True)
    value1_uom_sample1 = models.CharField(max_length=20, blank=True)
    value1_uom_sample2 = models.CharField(max_length=20, blank=True)
    value1_distinct_num = models.TextField(blank=True)  # This field type is a guess.
    value1_has_nulls = models.CharField(max_length=1, blank=True)
    value1_sample1 = models.CharField(max_length=110, blank=True)
    value1_sample2 = models.CharField(max_length=110, blank=True)
    value1_length_min = models.TextField(blank=True)  # This field type is a guess.
    value1_length_max = models.TextField(blank=True)  # This field type is a guess.
    value1_length_mean = models.TextField(blank=True)  # This field type is a guess.
    value1num_min = models.TextField(blank=True)  # This field type is a guess.
    value1num_max = models.TextField(blank=True)  # This field type is a guess.
    value1num_mean = models.TextField(blank=True)  # This field type is a guess.
    value1num_stddev = models.TextField(blank=True)  # This field type is a guess.
    value2_uom_num = models.TextField(blank=True)  # This field type is a guess.
    value2_uom_has_nulls = models.CharField(max_length=1, blank=True)
    value2_uom_sample1 = models.CharField(max_length=20, blank=True)
    value2_uom_sample2 = models.CharField(max_length=20, blank=True)
    value2_distinct_num = models.TextField(blank=True)  # This field type is a guess.
    value2_has_nulls = models.CharField(max_length=1, blank=True)
    value2_sample1 = models.CharField(max_length=110, blank=True)
    value2_sample2 = models.CharField(max_length=110, blank=True)
    value2_length_min = models.TextField(blank=True)  # This field type is a guess.
    value2_length_max = models.TextField(blank=True)  # This field type is a guess.
    value2_length_mean = models.TextField(blank=True)  # This field type is a guess.
    value2num_min = models.TextField(blank=True)  # This field type is a guess.
    value2num_max = models.TextField(blank=True)  # This field type is a guess.
    value2num_mean = models.TextField(blank=True)  # This field type is a guess.
    value2num_stddev = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'd_chartitems_detail'


class DCodeditems(models.Model):
    itemid = models.TextField(primary_key=True)  # This field type is a guess.
    code = models.CharField(max_length=10, blank=True)
    type = models.CharField(max_length=12, blank=True)
    category = models.CharField(max_length=13, blank=True)
    label = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'd_codeditems'


class DDemographicitems(models.Model):
    itemid = models.TextField(primary_key=True)  # This field type is a guess.
    label = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=19, blank=True)

    class Meta:
        managed = False
        db_table = 'd_demographicitems'


class DIoitems(models.Model):
    itemid = models.TextField(primary_key=True)  # This field type is a guess.
    label = models.CharField(max_length=600, blank=True)
    category = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'd_ioitems'


class DLabitems(models.Model):
    itemid = models.TextField(primary_key=True)  # This field type is a guess.
    test_name = models.CharField(max_length=50)
    fluid = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    loinc_code = models.CharField(max_length=7, blank=True)
    loinc_description = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'd_labitems'


class DMeditems(models.Model):
    itemid = models.TextField(primary_key=True)  # This field type is a guess.
    label = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'd_meditems'


class DParammapItems(models.Model):
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'd_parammap_items'


class DPatients(models.Model):
    subject_id = models.TextField(primary_key=True)  # This field type is a guess.
    sex = models.CharField(max_length=1, blank=True)
    dob = models.DateTimeField()
    dod = models.DateTimeField(blank=True, null=True)
    hospital_expire_flg = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'd_patients'


class DbSchema(models.Model):
    created_dt = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=15, blank=True)
    updated_dt = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=15, blank=True)
    schema_dt = models.DateTimeField(blank=True, null=True)
    version = models.CharField(max_length=25)
    comments = models.CharField(max_length=250, blank=True)

    class Meta:
        managed = False
        db_table = 'db_schema'


class Deliveries(models.Model):
    subject_id = models.TextField()  # This field type is a guess.
    icustay_id = models.TextField(blank=True)  # This field type is a guess.
    ioitemid = models.TextField()  # This field type is a guess.
    charttime = models.DateTimeField()
    elemid = models.TextField()  # This field type is a guess.
    cgid = models.TextField(blank=True)  # This field type is a guess.
    cuid = models.TextField(blank=True)  # This field type is a guess.
    site = models.CharField(max_length=20, blank=True)
    rate = models.TextField(blank=True)  # This field type is a guess.
    rateuom = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'deliveries'


class DemographicDetail(models.Model):
    subject_id = models.TextField()  # This field type is a guess.
    hadm_id = models.TextField()  # This field type is a guess.
    marital_status_itemid = models.TextField(blank=True)  # This field type is a guess.
    marital_status_descr = models.CharField(max_length=50, blank=True)
    ethnicity_itemid = models.TextField(blank=True)  # This field type is a guess.
    ethnicity_descr = models.CharField(max_length=50, blank=True)
    overall_payor_group_itemid = models.TextField(blank=True)  # This field type is a guess.
    overall_payor_group_descr = models.CharField(max_length=50, blank=True)
    religion_itemid = models.TextField(blank=True)  # This field type is a guess.
    religion_descr = models.CharField(max_length=50, blank=True)
    admission_type_itemid = models.TextField(blank=True)  # This field type is a guess.
    admission_type_descr = models.CharField(max_length=50, blank=True)
    admission_source_itemid = models.TextField(blank=True)  # This field type is a guess.
    admission_source_descr = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'demographic_detail'


class Demographicevents(models.Model):
    subject_id = models.TextField(primary_key=True)  # This field type is a guess.
    hadm_id = models.TextField(primary_key=True)  # This field type is a guess.
    itemid = models.TextField(primary_key=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'demographicevents'


class Drgevents(models.Model):
    subject_id = models.TextField(primary_key=True)  # This field type is a guess.
    hadm_id = models.TextField(primary_key=True)  # This field type is a guess.
    itemid = models.TextField(primary_key=True)  # This field type is a guess.
    cost_weight = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'drgevents'


class Icd9(models.Model):
    subject_id = models.TextField()  # This field type is a guess.
    hadm_id = models.TextField()  # This field type is a guess.
    sequence = models.TextField()  # This field type is a guess.
    code = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'icd9'


class IcustayDays(models.Model):
    icustay_id = models.TextField(blank=True)  # This field type is a guess.
    subject_id = models.TextField(blank=True)  # This field type is a guess.
    seq = models.TextField(blank=True)  # This field type is a guess.
    begintime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    first_day_flg = models.CharField(max_length=1, blank=True)
    last_day_flg = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'icustay_days'


class IcustayDetail(models.Model):
    icustay_id = models.TextField(blank=True)  # This field type is a guess.
    subject_id = models.TextField(blank=True)  # This field type is a guess.
    gender = models.CharField(max_length=1, blank=True)
    dob = models.DateTimeField()
    dod = models.DateTimeField(blank=True, null=True)
    expire_flg = models.CharField(max_length=1, blank=True)
    subject_icustay_total_num = models.TextField(blank=True)  # This field type is a guess.
    subject_icustay_seq = models.TextField(blank=True)  # This field type is a guess.
    hadm_id = models.TextField(blank=True)  # This field type is a guess.
    hospital_total_num = models.TextField(blank=True)  # This field type is a guess.
    hospital_seq = models.TextField(blank=True)  # This field type is a guess.
    hospital_first_flg = models.CharField(max_length=1, blank=True)
    hospital_last_flg = models.CharField(max_length=1, blank=True)
    hospital_admit_dt = models.DateTimeField(blank=True, null=True)
    hospital_disch_dt = models.DateTimeField(blank=True, null=True)
    hospital_los = models.TextField(blank=True)  # This field type is a guess.
    hospital_expire_flg = models.CharField(max_length=1, blank=True)
    icustay_total_num = models.TextField(blank=True)  # This field type is a guess.
    icustay_seq = models.TextField(blank=True)  # This field type is a guess.
    icustay_first_flg = models.CharField(max_length=1, blank=True)
    icustay_last_flg = models.CharField(max_length=1, blank=True)
    icustay_intime = models.DateTimeField()
    icustay_outtime = models.DateTimeField()
    icustay_admit_age = models.TextField(blank=True)  # This field type is a guess.
    icustay_age_group = models.CharField(max_length=7, blank=True)
    icustay_los = models.TextField()  # This field type is a guess.
    icustay_expire_flg = models.CharField(max_length=1, blank=True)
    icustay_first_careunit = models.CharField(max_length=20, blank=True)
    icustay_last_careunit = models.CharField(max_length=20, blank=True)
    icustay_first_service = models.CharField(max_length=110, blank=True)
    icustay_last_service = models.CharField(max_length=110, blank=True)
    height = models.TextField(blank=True)  # This field type is a guess.
    weight_first = models.TextField(blank=True)  # This field type is a guess.
    weight_min = models.TextField(blank=True)  # This field type is a guess.
    weight_max = models.TextField(blank=True)  # This field type is a guess.
    sapsi_first = models.TextField(blank=True)  # This field type is a guess.
    sapsi_min = models.TextField(blank=True)  # This field type is a guess.
    sapsi_max = models.TextField(blank=True)  # This field type is a guess.
    sofa_first = models.TextField(blank=True)  # This field type is a guess.
    sofa_min = models.TextField(blank=True)  # This field type is a guess.
    sofa_max = models.TextField(blank=True)  # This field type is a guess.
    matched_waveforms_num = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'icustay_detail'


class Icustayevents(models.Model):
    icustay_id = models.TextField(primary_key=True)  # This field type is a guess.
    subject_id = models.TextField()  # This field type is a guess.
    intime = models.DateTimeField()
    outtime = models.DateTimeField()
    los = models.TextField()  # This field type is a guess.
    first_careunit = models.TextField(blank=True)  # This field type is a guess.
    last_careunit = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'icustayevents'


class Ioevents(models.Model):
    subject_id = models.TextField()  # This field type is a guess.
    icustay_id = models.TextField(blank=True)  # This field type is a guess.
    itemid = models.TextField()  # This field type is a guess.
    charttime = models.DateTimeField()
    elemid = models.TextField()  # This field type is a guess.
    altid = models.TextField(blank=True)  # This field type is a guess.
    realtime = models.DateTimeField(blank=True, null=True)
    cgid = models.TextField(blank=True)  # This field type is a guess.
    cuid = models.TextField(blank=True)  # This field type is a guess.
    volume = models.TextField(blank=True)  # This field type is a guess.
    volumeuom = models.CharField(max_length=20, blank=True)
    unitshung = models.TextField(blank=True)  # This field type is a guess.
    unitshunguom = models.CharField(max_length=20, blank=True)
    newbottle = models.TextField(blank=True)  # This field type is a guess.
    stopped = models.CharField(max_length=20, blank=True)
    estimate = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'ioevents'


class Labevents(models.Model):
    subject_id = models.TextField()  # This field type is a guess.
    hadm_id = models.TextField(blank=True)  # This field type is a guess.
    icustay_id = models.TextField(blank=True)  # This field type is a guess.
    itemid = models.TextField()  # This field type is a guess.
    charttime = models.DateTimeField()
    value = models.CharField(max_length=100, blank=True)
    valuenum = models.TextField(blank=True)  # This field type is a guess.
    flag = models.CharField(max_length=10, blank=True)
    valueuom = models.CharField(max_length=10, blank=True)

    class Meta:
        managed = False
        db_table = 'labevents'


class Medevents(models.Model):
    subject_id = models.TextField()  # This field type is a guess.
    icustay_id = models.TextField(blank=True)  # This field type is a guess.
    itemid = models.TextField()  # This field type is a guess.
    charttime = models.DateTimeField()
    elemid = models.TextField()  # This field type is a guess.
    realtime = models.DateTimeField()
    cgid = models.TextField(blank=True)  # This field type is a guess.
    cuid = models.TextField(blank=True)  # This field type is a guess.
    volume = models.TextField(blank=True)  # This field type is a guess.
    dose = models.TextField(blank=True)  # This field type is a guess.
    doseuom = models.CharField(max_length=20, blank=True)
    solutionid = models.TextField(blank=True)  # This field type is a guess.
    solvolume = models.TextField(blank=True)  # This field type is a guess.
    solunits = models.CharField(max_length=20, blank=True)
    route = models.CharField(max_length=20, blank=True)
    stopped = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'medevents'


class Microbiologyevents(models.Model):
    subject_id = models.TextField(blank=True)  # This field type is a guess.
    hadm_id = models.TextField(blank=True)  # This field type is a guess.
    charttime = models.DateTimeField(blank=True, null=True)
    spec_itemid = models.TextField(blank=True)  # This field type is a guess.
    org_itemid = models.TextField(blank=True)  # This field type is a guess.
    isolate_num = models.TextField(blank=True)  # This field type is a guess.
    ab_itemid = models.TextField(blank=True)  # This field type is a guess.
    dilution_amount = models.CharField(max_length=72, blank=True)
    dilution_comparison = models.CharField(max_length=10, blank=True)
    interpretation = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'microbiologyevents'


class Noteevents(models.Model):
    subject_id = models.TextField()  # This field type is a guess.
    hadm_id = models.TextField(blank=True)  # This field type is a guess.
    icustay_id = models.TextField(blank=True)  # This field type is a guess.
    elemid = models.TextField(blank=True)  # This field type is a guess.
    charttime = models.DateTimeField()
    realtime = models.DateTimeField(blank=True, null=True)
    cgid = models.TextField(blank=True)  # This field type is a guess.
    correction = models.CharField(max_length=1, blank=True)
    cuid = models.TextField(blank=True)  # This field type is a guess.
    category = models.CharField(max_length=26, blank=True)
    title = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True)
    exam_name = models.CharField(max_length=100, blank=True)
    patient_info = models.CharField(max_length=4000, blank=True)

    class Meta:
        managed = False
        db_table = 'noteevents'


class ParameterMapping(models.Model):
    param1_str = models.CharField(max_length=50, blank=True)
    param1_num = models.TextField(blank=True)  # This field type is a guess.
    category = models.CharField(max_length=50)
    param2_str = models.CharField(max_length=50, blank=True)
    param2_num = models.TextField(blank=True)  # This field type is a guess.
    order_num = models.TextField(blank=True)  # This field type is a guess.
    valid_flg = models.CharField(max_length=1)
    comments = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'parameter_mapping'


class PoeMed(models.Model):
    poe_id = models.TextField()  # This field type is a guess.
    drug_type = models.CharField(max_length=20)
    drug_name = models.CharField(max_length=100)
    drug_name_generic = models.CharField(max_length=100, blank=True)
    prod_strength = models.CharField(max_length=255, blank=True)
    form_rx = models.CharField(max_length=25, blank=True)
    dose_val_rx = models.CharField(max_length=100, blank=True)
    dose_unit_rx = models.CharField(max_length=50, blank=True)
    form_val_disp = models.CharField(max_length=50, blank=True)
    form_unit_disp = models.CharField(max_length=50, blank=True)
    dose_val_disp = models.TextField(blank=True)  # This field type is a guess.
    dose_unit_disp = models.CharField(max_length=50, blank=True)
    dose_range_override = models.CharField(max_length=2000, blank=True)

    class Meta:
        managed = False
        db_table = 'poe_med'


class PoeOrder(models.Model):
    poe_id = models.TextField(primary_key=True)  # This field type is a guess.
    subject_id = models.TextField()  # This field type is a guess.
    hadm_id = models.TextField()  # This field type is a guess.
    icustay_id = models.TextField(blank=True)  # This field type is a guess.
    start_dt = models.DateTimeField(blank=True, null=True)
    stop_dt = models.DateTimeField(blank=True, null=True)
    enter_dt = models.DateTimeField()
    medication = models.CharField(max_length=255, blank=True)
    procedure_type = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=50, blank=True)
    route = models.CharField(max_length=50, blank=True)
    frequency = models.CharField(max_length=50, blank=True)
    dispense_sched = models.CharField(max_length=255, blank=True)
    iv_fluid = models.CharField(max_length=255, blank=True)
    iv_rate = models.CharField(max_length=100, blank=True)
    infusion_type = models.CharField(max_length=15, blank=True)
    sliding_scale = models.CharField(max_length=1, blank=True)
    doses_per_24hrs = models.TextField(blank=True)  # This field type is a guess.
    duration = models.TextField(blank=True)  # This field type is a guess.
    duration_intvl = models.CharField(max_length=15, blank=True)
    expiration_val = models.TextField(blank=True)  # This field type is a guess.
    expiration_unit = models.CharField(max_length=50, blank=True)
    expiration_dt = models.DateTimeField(blank=True, null=True)
    label_instr = models.CharField(max_length=1000, blank=True)
    additional_instr = models.CharField(max_length=1000, blank=True)
    md_add_instr = models.CharField(max_length=4000, blank=True)
    rnurse_add_instr = models.CharField(max_length=1000, blank=True)

    class Meta:
        managed = False
        db_table = 'poe_order'


class Procedureevents(models.Model):
    subject_id = models.TextField(primary_key=True)  # This field type is a guess.
    hadm_id = models.TextField(primary_key=True)  # This field type is a guess.
    itemid = models.TextField(blank=True)  # This field type is a guess.
    sequence_num = models.TextField(primary_key=True)  # This field type is a guess.
    proc_dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procedureevents'


class Totalbalevents(models.Model):
    subject_id = models.TextField()  # This field type is a guess.
    icustay_id = models.TextField(blank=True)  # This field type is a guess.
    itemid = models.TextField()  # This field type is a guess.
    charttime = models.DateTimeField()
    elemid = models.TextField()  # This field type is a guess.
    realtime = models.DateTimeField()
    cgid = models.TextField(blank=True)  # This field type is a guess.
    cuid = models.TextField(blank=True)  # This field type is a guess.
    pervolume = models.TextField(blank=True)  # This field type is a guess.
    cumvolume = models.TextField(blank=True)  # This field type is a guess.
    accumperiod = models.CharField(max_length=20, blank=True)
    approx = models.CharField(max_length=20, blank=True)
    reset = models.TextField(blank=True)  # This field type is a guess.
    stopped = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'totalbalevents'
