# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('agegroupID', models.AutoField(primary_key=True, serialize=False)),
                ('agegroup', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['agegroupID'],
            },
        ),
        migrations.CreateModel(
            name='Avatars',
            fields=[
                ('avatarID', models.IntegerField(primary_key=True, serialize=False)),
                ('avatarImage', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Corebelief',
            fields=[
                ('corebeliefID', models.IntegerField(primary_key=True, serialize=False)),
                ('corebelief_text', models.TextField()),
            ],
            options={
                'ordering': ['corebeliefID'],
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('countryID', models.IntegerField(primary_key=True, serialize=False)),
                ('country_Name', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['country_Name'],
            },
        ),
        migrations.CreateModel(
            name='Customuserprofile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('gender', models.CharField(max_length=10, choices=[('female', 'FEMALE'), ('male', 'MALE'), ('other', 'OTHER')])),
                ('phonenumber', models.CharField(max_length=10)),
                ('agegroup', models.ForeignKey(to='cbt2.Age')),
                ('avatar', models.ForeignKey(default=1, to='cbt2.Avatars')),
                ('country', models.ForeignKey(to='cbt2.Countries')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('educationID', models.IntegerField(primary_key=True, serialize=False)),
                ('education_qualification', models.CharField(null=True, max_length=20, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Eventlist',
            fields=[
                ('eventID', models.IntegerField(primary_key=True, serialize=False)),
                ('event_text', models.TextField()),
            ],
            options={
                'ordering': ['eventID'],
            },
        ),
        migrations.CreateModel(
            name='Familymembers',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('member_name', models.CharField(verbose_name='Name', max_length=200)),
                ('relate', models.CharField(default='', verbose_name='Relation to you', max_length=50)),
                ('emailid', models.EmailField(null=True, verbose_name='Email ID', max_length=25, blank=True)),
                ('phonenumber', models.CharField(null=True, verbose_name='Phone Number', max_length=10, blank=True)),
                ('involvementid', models.IntegerField(default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Intermediatebelief',
            fields=[
                ('intermediatebeliefID', models.IntegerField(primary_key=True, serialize=False)),
                ('intermediatebelief_text', models.TextField()),
            ],
            options={
                'ordering': ['intermediatebeliefID'],
            },
        ),
        migrations.CreateModel(
            name='Occupations',
            fields=[
                ('occupationID', models.AutoField(primary_key=True, serialize=False)),
                ('occupation_name', models.CharField(null=True, max_length=20, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persistentnat',
            fields=[
                ('persistentnatID', models.IntegerField(primary_key=True, serialize=False)),
                ('persistentnat_text', models.TextField()),
            ],
            options={
                'ordering': ['persistentnatID'],
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('dsasweek1', models.CharField(null=True, max_length=50, blank=True)),
                ('dsasweek2', models.CharField(null=True, max_length=50, blank=True)),
                ('dsasweek3', models.CharField(null=True, max_length=50, blank=True)),
                ('dsasweek4', models.CharField(null=True, max_length=50, blank=True)),
                ('dsasweek5', models.CharField(null=True, max_length=50, blank=True)),
                ('asweek1', models.CharField(null=True, max_length=50, blank=True)),
                ('asweek2', models.CharField(null=True, max_length=50, blank=True)),
                ('asweek3', models.CharField(null=True, max_length=50, blank=True)),
                ('asweek4', models.CharField(null=True, max_length=50, blank=True)),
                ('asweek5', models.CharField(null=True, max_length=50, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Userevent',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('chaeck', models.BooleanField(default=False)),
                ('event', models.ForeignKey(to='cbt2.Eventlist')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Userpnat',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('persistentnat', models.ForeignKey(to='cbt2.Persistentnat')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Userscb',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('corebelief', models.ForeignKey(to='cbt2.Corebelief')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Usersib',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('intermediatebelief', models.ForeignKey(to='cbt2.Intermediatebelief')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='persistentnat',
            name='persistentnats',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='cbt2.Userpnat'),
        ),
        migrations.AddField(
            model_name='intermediatebelief',
            name='intermediatebeliefs',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='cbt2.Usersib'),
        ),
        migrations.AddField(
            model_name='eventlist',
            name='event',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='cbt2.Userevent'),
        ),
        migrations.AddField(
            model_name='customuserprofile',
            name='education',
            field=models.ForeignKey(to='cbt2.Education'),
        ),
        migrations.AddField(
            model_name='customuserprofile',
            name='enrolled_as',
            field=models.ForeignKey(to='cbt2.Occupations'),
        ),
        migrations.AddField(
            model_name='customuserprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='corebelief',
            name='corebeliefs',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='cbt2.Userscb'),
        ),
    ]
