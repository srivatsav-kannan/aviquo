# Generated by Django 4.2.5 on 2023-09-20 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_oldextracurricular_alter_extracurricular_cost_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='extracurricular',
            name='Grade',
            field=models.IntegerField(choices=[(1, '9'), (2, '10'), (3, '11'), (4, '12'), (5, 'All Grades')], default=None, null=True),
        ),
        migrations.AddField(
            model_name='extracurricular',
            name='Location',
            field=models.IntegerField(choices=[(1, 'Usa'), (2, 'Global')], default=None, null=True),
        ),
        migrations.AddField(
            model_name='extracurricular',
            name='Offered By',
            field=models.IntegerField(choices=[(1, 'Educational Insitution'), (2, 'Nonprofit Organization'), (3, 'Business Corporation')], default=None, null=True),
        ),
        migrations.AddField(
            model_name='extracurricular',
            name='Organization',
            field=models.IntegerField(choices=[(1, 'Club'), (2, 'Program')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='extracurricular',
            name='selectivity',
            field=models.IntegerField(choices=[(1, 'Less Selective'), (2, 'Medium Selective'), (3, 'Very Selective')], default=None, null=True),
        ),
    ]
