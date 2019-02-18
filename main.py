#!/usr/bin/python
#! -*- coding:utf-8 -*-

import datetime
import os
import re
import yaml
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
os.environ["DJANGO_SETTINGS_MODULE"] = 'admin.settings.local_cj' #因为有线上环境和测试环境两个数据库，需要两个配置文件
import django
import time
django.setup()
from scanhosts.models import HostInfo
from scanhosts.util.nmap_all_servers import nmap_begin
from scanhosts.util.nmap_all_servers import
from scanhosts.util.nmap_docker import nmap_docker

