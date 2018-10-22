# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-11 15:54
from __future__ import unicode_literals

import awx.main.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import oauth2_provider.generators

# TODO: Squash all of these migrations with '0024_v330_add_oauth_activity_stream_registrar'

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_v330_polymorphic_delete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oauth2accesstoken',
            name='scope',
            field=models.TextField(blank=True, default='write', help_text="Allowed scopes, further restricts user's permissions."),
        ),
        migrations.AlterField(
            model_name='oauth2accesstoken',
            name='user',
            field=models.ForeignKey(blank=True, help_text='The user representing the token owner', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_oauth2accesstoken', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='oauth2application',
            name='authorization_grant_type',
            field=models.CharField(choices=[('authorization-code', 'Authorization code'), ('implicit', 'Implicit'), ('password', 'Resource owner password-based'), ('client-credentials', 'Client credentials')], help_text='The Grant type the user must use for acquire tokens for this application.', max_length=32),
        ),
        migrations.AlterField(
            model_name='oauth2application',
            name='client_secret',
            field=awx.main.fields.OAuth2ClientSecretField(blank=True, db_index=True, default=oauth2_provider.generators.generate_client_secret, help_text='Used for more stringent verification of access to an application when creating a token.', max_length=1024),
        ),
        migrations.AlterField(
            model_name='oauth2application',
            name='client_type',
            field=models.CharField(choices=[('confidential', 'Confidential'), ('public', 'Public')], help_text='Set to Public or Confidential depending on how secure the client device is.', max_length=32),
        ),
        migrations.AlterField(
            model_name='oauth2application',
            name='skip_authorization',
            field=models.BooleanField(default=False, help_text='Set True to skip authorization step for completely trusted applications.'),
        ),
    ]
