# Generated by Django 2.2.13 on 2020-12-19 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0004_exam_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='result.Exam'),
        ),
    ]
