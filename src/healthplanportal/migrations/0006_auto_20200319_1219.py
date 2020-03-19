# Generated by Django 3.0.1 on 2020-03-19 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthplanportal', '0005_auto_20200319_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthplan',
            name='Diagnostic_test_lab',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Diagnostic_test_xray',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Durable_medical_eqiupment',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Emergency_medical_transportation_HospitalStay',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Emergency_medical_transportation_IMA',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Emergency_room_care_Hospital_Stay',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Emergency_room_care_IMA',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Facility_fee',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Generic_drugs_pescrciption',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Home_health_care',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Imaging',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Inpatient_services',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Out_of_pocket_limit_family',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Out_of_pocket_limit_person',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Outpatient_services',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Overall_deductible_family',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Overall_deductible_person',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Physician_surgeon_fee',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Preffered_drugs_pescrciption',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Pregnant_childbirth_delivery_facility_services',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Pregnant_childbirth_delivery_professional_services',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Pregnant_office_visit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Primary_care_visit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Rehabilitation_services',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Skilled_nursing_care',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Specialist_visit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Urgent_care_IMA',
            field=models.IntegerField(),
        ),
    ]
