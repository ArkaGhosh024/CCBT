# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conversationmanager', '0002_auto_20150627_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversationoptiongraph',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Conversations',
            fields=[
                ('conversationID', models.IntegerField()),
                ('dialog', models.IntegerField(serialize=False, verbose_name='dialog ID', primary_key=True)),
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
                ('option_text', models.TextField()),
            ],
            options={
                'ordering': ['optionID'],
            },
        ),
        migrations.CreateModel(
            name='Userconversation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
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
            field=models.ManyToManyField(through='conversationmanager.Conversationoptiongraph', to='conversationmanager.Options'),
        ),
        migrations.AddField(
            model_name='conversations',
            name='user_conversation',
            field=models.ManyToManyField(through='conversationmanager.Userconversation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='conversationoptiongraph',
            name='current_dialog',
            field=models.ForeignKey(to='conversationmanager.Conversations'),
        ),
        migrations.AddField(
            model_name='conversationoptiongraph',
            name='next_dialog',
            field=models.ForeignKey(related_name='next_dialog', null=True, blank=True, to='conversationmanager.Conversations'),
        ),
        migrations.AddField(
            model_name='conversationoptiongraph',
            name='option',
            field=models.ForeignKey(to='conversationmanager.Options'),
        ),
    ]
