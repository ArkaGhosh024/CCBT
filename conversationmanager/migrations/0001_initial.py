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
            name='Conversationoption',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Conversations',
            fields=[
                ('conversationID', models.IntegerField()),
                ('dialog', models.IntegerField(serialize=False, primary_key=True, verbose_name='dialog ID')),
                ('dialog_text', models.TextField()),
            ],
            options={
                'ordering': ['dialog'],
            },
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('optionID', models.IntegerField(serialize=False, primary_key=True)),
                ('option_text', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ['optionID'],
            },
        ),
        migrations.CreateModel(
            name='Userconversation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('conversationID', models.IntegerField()),
                ('conversation_time', models.DateTimeField()),
                ('conversation', models.ForeignKey(to='conversationmanager.Conversations')),
                ('option_selected', models.ForeignKey(to='conversationmanager.Options')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-conversation_time', 'user'],
            },
        ),
        migrations.AddField(
            model_name='conversations',
            name='option',
            field=models.ManyToManyField(through='conversationmanager.Conversationoption', to='conversationmanager.Options'),
        ),
        migrations.AddField(
            model_name='conversations',
            name='user_conversation',
            field=models.ManyToManyField(through='conversationmanager.Userconversation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='conversationoption',
            name='current_conversation',
            field=models.ForeignKey(to='conversationmanager.Conversations'),
        ),
        migrations.AddField(
            model_name='conversationoption',
            name='next_conversation',
            field=models.ForeignKey(to='conversationmanager.Conversations', null=True, related_name='next_conversation', blank=True),
        ),
        migrations.AddField(
            model_name='conversationoption',
            name='option',
            field=models.ForeignKey(to='conversationmanager.Options'),
        ),
    ]
