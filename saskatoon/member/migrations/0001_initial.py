# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-19 02:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name=b'email address')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('actor_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'actor',
                'verbose_name_plural': 'actors',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'city',
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_fr', models.CharField(max_length=150, null=True, verbose_name='Name')),
                ('name_en', models.CharField(max_length=150, null=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'language',
                'verbose_name_plural': 'languages',
            },
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_fr', models.CharField(max_length=150, null=True, verbose_name='Name')),
                ('name_en', models.CharField(max_length=150, null=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'neighborhood',
                'verbose_name_plural': 'neighborhoods',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'states',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('actor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='member.Actor')),
                ('redmine_contact_id', models.IntegerField(blank=True, null=True, verbose_name='Redmine contact')),
                ('civil_name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('phone', models.CharField(max_length=50, null=True, verbose_name='Phone')),
                ('contact_person_role', models.CharField(blank=True, max_length=50, null=True, verbose_name='Contact person role')),
                ('street_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Number')),
                ('street', models.CharField(blank=True, max_length=50, null=True, verbose_name='Street')),
                ('complement', models.CharField(blank=True, max_length=150, null=True, verbose_name='Complement')),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Postal code')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
                ('city', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.City', verbose_name='City')),
            ],
            options={
                'verbose_name': 'organization',
                'verbose_name_plural': 'organizations',
            },
            bases=('member.actor',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('actor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='member.Actor')),
                ('redmine_contact_id', models.IntegerField(blank=True, null=True, verbose_name='Redmine contact')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('family_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Family name')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='Phone')),
                ('street_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Number')),
                ('street', models.CharField(blank=True, max_length=50, null=True, verbose_name='Street')),
                ('complement', models.CharField(blank=True, max_length=150, null=True, verbose_name='Complement')),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Postal code')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
                ('comments', models.TextField(blank=True, verbose_name='Comments')),
                ('city', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.City', verbose_name='City')),
                ('country', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Country', verbose_name='Country')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Language', verbose_name='Preferred language')),
                ('neighborhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Neighborhood', verbose_name='Neighborhood')),
                ('state', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.State', verbose_name='State')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'people',
            },
            bases=('member.actor',),
        ),
        migrations.AddField(
            model_name='organization',
            name='contact_person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Person', verbose_name='Contact person'),
        ),
        migrations.AddField(
            model_name='organization',
            name='country',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Country', verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='organization',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Neighborhood', verbose_name='Neighborhood'),
        ),
        migrations.AddField(
            model_name='organization',
            name='state',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.State', verbose_name='State'),
        ),
        migrations.AddField(
            model_name='authuser',
            name='person',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Person'),
        ),
    ]
