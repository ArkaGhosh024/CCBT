# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConversationToConversation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('technique', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConversationToModule',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('module_number', models.IntegerField()),
                ('correct_technique', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseConversation',
            fields=[
                ('conversationID', models.IntegerField(serialize=False, primary_key=True)),
                ('conversation_text', models.TextField()),
                ('conversation_type', models.CharField(default='Base', max_length=255)),
            ],
            options={
                'ordering': ['conversationID'],
            },
        ),
        migrations.AddField(
            model_name='conversationtomodule',
            name='conversation',
            field=models.ForeignKey(null=True, related_name='conversation', to='exercise.ExerciseConversation'),
        ),
        migrations.AddField(
            model_name='conversationtoconversation',
            name='base_conversation',
            field=models.ForeignKey(null=True, related_name='base_conversation', to='exercise.ExerciseConversation'),
        ),
        migrations.AddField(
            model_name='conversationtoconversation',
            name='technique_conversation',
            field=models.ForeignKey(null=True, related_name='technique_conversation', to='exercise.ExerciseConversation'),
        ),
    ]
