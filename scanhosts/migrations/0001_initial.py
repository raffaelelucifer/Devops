# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DockerInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=30, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u4e3b\u673a\u540d')),
                ('ip', models.CharField(max_length=20, verbose_name='\u6240\u5c5e\u673a\u5668\u7684ip')),
                ('docker_id', models.CharField(max_length=30, verbose_name='\u5bb9\u5668ID')),
                ('port', models.CharField(max_length=10, null=True, verbose_name='\u6620\u5c04\u7aef\u53e3')),
                ('service', models.CharField(max_length=50, verbose_name='\u8fd0\u884c\u670d\u52a1')),
            ],
            options={
                'db_table': 'DockerInfo',
                'verbose_name': 'Docker\u5bb9\u5668\u4fe1\u606f\u8868',
                'verbose_name_plural': 'Docker\u5bb9\u5668\u4fe1\u606f\u8868',
            },
        ),
        migrations.CreateModel(
            name='HostInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=20, verbose_name='\u4e3b\u673aIP')),
                ('hostname', models.CharField(max_length=30, verbose_name='\u4e3b\u673a\u540d')),
                ('port', models.CharField(max_length=10, verbose_name='\u767b\u5f55\u7aef\u53e3')),
                ('user', models.CharField(max_length=30, verbose_name='\u767b\u5f55\u7528\u6237')),
                ('ssh_key', models.CharField(max_length=124, verbose_name='\u767b\u5f55\u79d8\u94a5')),
                ('system_version', models.CharField(max_length=200, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u7248\u672c')),
                ('sn', models.CharField(max_length=30, verbose_name='\u8bbe\u5907\u5e8f\u5217\u53f7')),
                ('mac', models.CharField(max_length=30, verbose_name='\u8bbe\u5907\u7269\u7406\u5730\u5740')),
                ('host_type', models.CharField(max_length=200, verbose_name='\u4e3b\u673a\u7c7b\u578b')),
            ],
            options={
                'db_table': 'HostInfo',
                'verbose_name': '\u521d\u59cb\u5316\u626b\u63cf\u4fe1\u606f\u8868',
                'verbose_name_plural': '\u521d\u59cb\u5316\u626b\u63cf\u4fe1\u606f\u8868',
            },
        ),
    ]
