# Generated by Django 5.0.6 on 2024-09-20 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subone', '0082_industryweservelist_industryweserve_industry_lists'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerfeedbackform',
            old_name='date',
            new_name='assessment_date',
        ),
        migrations.RenameField(
            model_name='customerfeedbackform',
            old_name='audit_standard',
            new_name='assessment_standard',
        ),
        migrations.RenameField(
            model_name='customerfeedbackform',
            old_name='audit_type',
            new_name='assessment_team_members',
        ),
        migrations.RenameField(
            model_name='customerfeedbackform',
            old_name='company_activities',
            new_name='assessment_type',
        ),
        migrations.RenameField(
            model_name='customerfeedbackform',
            old_name='lead_auditor_name',
            new_name='business_activities',
        ),
        migrations.RenameField(
            model_name='customerfeedbackform',
            old_name='feedback_audit_team',
            new_name='feedback_assessment_team',
        ),
        migrations.RenameField(
            model_name='customerfeedbackform',
            old_name='other_audit_team_name',
            new_name='lead_assessor_name',
        ),
    ]