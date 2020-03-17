# Generated by Django 2.2.6 on 2020-03-17 21:19

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='demographics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Non-Binary')], default='Unspecified', max_length=500)),
                ('Age', models.CharField(choices=[('4', '18-24'), ('5', '25-34'), ('6', '35-44'), ('7', '45-54'), ('7', '55-65+')], default='Unspecified', max_length=500)),
                ('Height', models.CharField(choices=[('8', "<4'7/140 cm"), ('9', "4'8 - 4'11/ 141-150cm"), ('10', "4'11 - 5'3/ 151-160cm"), ('11', "5'3 - 5'7/ 161-170cm"), ('12', "5'7 - 5'11/ 171-180cm"), ('13', "5'11 - 6'3/ 181-190cm"), ('14', "<6'3 /190cm ")], default='Unspecified', max_length=500)),
                ('Weight', models.CharField(choices=[('15', '100-120 pounds'), ('16', '120-140 pounds'), ('17', '140-160 pounds'), ('18', '160-180 pounds'), ('19', '180-200 pounds'), ('20', '200-220 pounds'), ('21', '220-240 pounds'), ('22', '240-260+ pounds')], default='Unspecified', max_length=500)),
                ('Activity_Level', models.CharField(choices=[('23', 'I excercise 1-2 days a week'), ('24', 'I excercise 2-4 days a week'), ('25', 'I excercise 4-6 days a week')], default='Unspecified', max_length=500)),
                ('Level_of_excerise', models.CharField(choices=[('26', 'Light- walking, jogging, etc...'), ('27', 'Moderate- dancing, biking, use weights, etc...'), ('28', 'Hard - swimming, running, etc...')], default='Unspecified', max_length=500)),
                ('Do_you_smoke', models.CharField(choices=[('29', 'Yes'), ('30', 'No')], default='Unspecified', max_length=500)),
                ('Do_you_take_non_presribed_drugs', models.CharField(choices=[('29', 'Yes'), ('30', 'No')], default='Unspecified', max_length=500)),
                ('Do_you_often_participate_in_sports', models.CharField(choices=[('31', 'Yes'), ('32', 'No')], default='Unspecified', max_length=500)),
                ('Do_you_have_a_labor_intensive_job', models.CharField(choices=[('33', 'Yes'), ('34', 'No')], default='Unspecified', max_length=500)),
                ('Please_choose_all_that_apply', multiselectfield.db.fields.MultiSelectField(choices=[('Depression/or other mental health conditions', 'Depression/or other mental health conditions'), ('Respiratory Illnesses', 'Respiratory Illnesses'), ('Heart condition(s)', 'Heart Condition(s)'), ('Have dependencies', 'Have dependencies'), ('Take prescription drugs', 'Take prescription drugs'), ('Diabetes', 'Diabetes'), ('Physical condition(s)', 'Physical condition(s)'), ('Chronic Condition(s)', 'Chronic Condition(s)'), ('Disabled', 'Disabled'), ('Serious illnesses and disorders(HIV/Aids, Cancer ,Influenza, Scoliosis, Epilepsy, etc..)', 'Serious illnesses and disorders(HIV/Aids, Cancer ,Influenza, Scoliosis, Epilepsy, etc..)')], default='Unspecified', max_length=100)),
            ],
        ),
    ]
