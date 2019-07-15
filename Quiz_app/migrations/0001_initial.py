# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-14 12:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='qusetion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(null=True)),
                ('Year', models.CharField(choices=[(b'1', b'1st'), (b'2', b'2nd'), (b'3', b'3rd'), (b'4', b'4th'), (b'M', b'Mtech')], default=b'1', max_length=1)),
                ('event', models.CharField(default=b'gk', max_length=100)),
                ('data', models.CharField(max_length=1000, null=True)),
                ('opt1', models.CharField(max_length=200, null=True)),
                ('opt2', models.CharField(max_length=200, null=True)),
                ('opt3', models.CharField(max_length=200, null=True)),
                ('opt4', models.CharField(max_length=200, null=True)),
                ('ans', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='sets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(null=True, unique=True)),
                ('set2_val', models.IntegerField(blank=True, null=True)),
                ('set3_val', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='userprof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roll_No', models.CharField(max_length=40, null=True)),
                ('Year', models.CharField(default=b'1', max_length=1)),
                ('Score', models.IntegerField(default=0, null=True)),
                ('time', models.IntegerField(null=True)),
                ('set', models.IntegerField(blank=True, null=True)),
                ('given', models.BooleanField(default=False)),
                ('q1', models.IntegerField(default=0, null=True)),
                ('q2', models.IntegerField(default=0, null=True)),
                ('q3', models.IntegerField(default=0, null=True)),
                ('q4', models.IntegerField(default=0, null=True)),
                ('q5', models.IntegerField(default=0, null=True)),
                ('q6', models.IntegerField(default=0, null=True)),
                ('q7', models.IntegerField(default=0, null=True)),
                ('q8', models.IntegerField(default=0, null=True)),
                ('q9', models.IntegerField(default=0, null=True)),
                ('q10', models.IntegerField(default=0, null=True)),
                ('q11', models.IntegerField(default=0, null=True)),
                ('q12', models.IntegerField(default=0, null=True)),
                ('q13', models.IntegerField(default=0, null=True)),
                ('q14', models.IntegerField(default=0, null=True)),
                ('q15', models.IntegerField(default=0, null=True)),
                ('q16', models.IntegerField(default=0, null=True)),
                ('q17', models.IntegerField(default=0, null=True)),
                ('q18', models.IntegerField(default=0, null=True)),
                ('q19', models.IntegerField(default=0, null=True)),
                ('q20', models.IntegerField(default=0, null=True)),
                ('q21', models.IntegerField(default=0, null=True)),
                ('q22', models.IntegerField(default=0, null=True)),
                ('q23', models.IntegerField(default=0, null=True)),
                ('q24', models.IntegerField(default=0, null=True)),
                ('q25', models.IntegerField(default=0, null=True)),
                ('q26', models.IntegerField(default=0, null=True)),
                ('q27', models.IntegerField(default=0, null=True)),
                ('q28', models.IntegerField(default=0, null=True)),
                ('q29', models.IntegerField(default=0, null=True)),
                ('q30', models.IntegerField(default=0, null=True)),
                ('q31', models.IntegerField(default=0, null=True)),
                ('q32', models.IntegerField(default=0, null=True)),
                ('q33', models.IntegerField(default=0, null=True)),
                ('q34', models.IntegerField(default=0, null=True)),
                ('q35', models.IntegerField(default=0, null=True)),
                ('q36', models.IntegerField(default=0, null=True)),
                ('q37', models.IntegerField(default=0, null=True)),
                ('q38', models.IntegerField(default=0, null=True)),
                ('q39', models.IntegerField(default=0, null=True)),
                ('q40', models.IntegerField(default=0, null=True)),
                ('q41', models.IntegerField(default=0, null=True)),
                ('q42', models.IntegerField(default=0, null=True)),
                ('q43', models.IntegerField(default=0, null=True)),
                ('q44', models.IntegerField(default=0, null=True)),
                ('q45', models.IntegerField(default=0, null=True)),
                ('q46', models.IntegerField(default=0, null=True)),
                ('q47', models.IntegerField(default=0, null=True)),
                ('q48', models.IntegerField(default=0, null=True)),
                ('q49', models.IntegerField(default=0, null=True)),
                ('q50', models.IntegerField(default=0, null=True)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='qusetion',
            unique_together=set([('Year', 'no', 'event')]),
        ),
    ]