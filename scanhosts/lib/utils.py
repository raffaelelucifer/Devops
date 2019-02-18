#!/usr/bin/python
# -*- encoding: utf-8 -*-

import re

def mac_trans(mac):
    if mac:
        mac_lst = mac.split('\n')
        mac_res = [item.replace(':','').replace("000000000000",'').replace("00000000", '') for item in mac_lst]
        mac_string = '_'.join(mac_res)
        return mac_string
    else:
        return ""

def sn_trans(sn):
    if sn:
        sn_res = sn.replace(" ",'')
        return sn_res
    else:
        return ""

def machine_type_trans(mt):
    if mt:
        mt_res = mt.replace("\n", '')
        return mt_res
    else:
        return ""

def getsysversion(version_list):
    for version_data in [version_list]:
        v_data_lst = re.findall("vmware|centos|ubuntu|linux|redhat|\d{1,}\.\d{1,}", version_data, re.IGNORECASE)
        if v_data_lst:
            if len(v_data_lst) > 1:
                v_data = " ".join(v_data_lst)
                break
        else:
            v_data = ""
    return v_data
