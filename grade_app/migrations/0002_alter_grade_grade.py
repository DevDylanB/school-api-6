# Generated by Django 5.0.3 on 2024-03-30 18:15

import grade_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=5, validators=[grade_app.validators.validate_grade_limit]),
        ),
    ]
