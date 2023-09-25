# Generated by Django 4.2.5 on 2023-09-23 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_category_grade_remove_category_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='awardreference',
            name='grade',
            field=models.IntegerField(choices=[(1, '9'), (2, '10'), (3, '11'), (4, '12'), (5, 'All')], null=True),
        ),
        migrations.AddField(
            model_name='awardreference',
            name='location',
            field=models.IntegerField(choices=[(1, 'USA'), (2, 'Global')], null=True),
        ),
        migrations.AddField(
            model_name='awardreference',
            name='offered_by',
            field=models.IntegerField(choices=[(1, 'Educational_Institution'), (2, 'Non-profit_Organization'), (3, 'Business_Corporation')], null=True),
        ),
        migrations.AddField(
            model_name='extracurricularreference',
            name='grade',
            field=models.IntegerField(choices=[(1, '9'), (2, '10'), (3, '11'), (4, '12'), (5, 'All')], null=True),
        ),
        migrations.AddField(
            model_name='extracurricularreference',
            name='location',
            field=models.IntegerField(choices=[(1, 'USA'), (2, 'Global')], null=True),
        ),
        migrations.AddField(
            model_name='extracurricularreference',
            name='offered_by',
            field=models.IntegerField(choices=[(1, 'Educational_Institution'), (2, 'Non-profit_Organization'), (3, 'Business_Corporation')], null=True),
        ),
        migrations.AddField(
            model_name='scholarshipreference',
            name='grade',
            field=models.IntegerField(choices=[(1, '9'), (2, '10'), (3, '11'), (4, '12'), (5, 'All')], null=True),
        ),
        migrations.AddField(
            model_name='scholarshipreference',
            name='location',
            field=models.IntegerField(choices=[(1, 'USA'), (2, 'Global')], null=True),
        ),
        migrations.AddField(
            model_name='scholarshipreference',
            name='offered_by',
            field=models.IntegerField(choices=[(1, 'Educational_Institution'), (2, 'Non-profit_Organization'), (3, 'Business_Corporation')], null=True),
        ),
        migrations.AlterField(
            model_name='awardreference',
            name='field',
            field=models.IntegerField(choices=[(1, 'Computer Science'), (2, 'Engineering'), (3, 'Mathematics'), (4, 'Medicine'), (5, 'Business'), (6, 'Law'), (7, 'Politics'), (8, 'History'), (9, 'Arts'), (10, 'Writing'), (11, 'Psychology'), (12, 'Environment'), (13, 'Architecture')], null=True),
        ),
        migrations.AlterField(
            model_name='extracurricularreference',
            name='field',
            field=models.IntegerField(choices=[(1, 'Computer Science'), (2, 'Engineering'), (3, 'Mathematics'), (4, 'Medicine'), (5, 'Business'), (6, 'Law'), (7, 'Politics'), (8, 'History'), (9, 'Arts'), (10, 'Writing'), (11, 'Psychology'), (12, 'Environment'), (13, 'Architecture')], null=True),
        ),
        migrations.AlterField(
            model_name='scholarshipreference',
            name='field',
            field=models.IntegerField(choices=[(1, 'Computer Science'), (2, 'Engineering'), (3, 'Mathematics'), (4, 'Medicine'), (5, 'Business'), (6, 'Law'), (7, 'Politics'), (8, 'History'), (9, 'Arts'), (10, 'Writing'), (11, 'Psychology'), (12, 'Environment'), (13, 'Architecture')], null=True),
        ),
    ]
