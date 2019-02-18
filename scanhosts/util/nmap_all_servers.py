#!/usr/bin/python
# -*- coding:utf8 -*-

import os,sys
PROJECT_ROOT = '/root/Devops'
sys.path.insert(0,PROJECT_ROOT)
os.environ["DJANGO_SETTINGS_MODULE"] = 'Devops.settings'
import django
django.setup()

import os

os.environ["DJANGO_SETTINGS_MODULE"] = 'Devops.settings'

import django
from django.conf import settings
from scanhosts.lib.J_do import J_ssh_do
from scanhosts.lib.utils import mac_trans, sn_trans, machine_type_trans, getsysversion
import nmap
import os
import re
import telnetlib
import yaml
from scanhosts.models import HostInfo
from django.core.mail import EmailMessage, send_mail

import logging
logger = logging.getLogger("django")

myconf = yaml.load(file('../../conf/scanhosts.yaml'))

#def nmap_begin(nmap_type, keyfile, ports, cmd_list, black_list, s_emails):
def nmap_begin(nmap_type, keyfile, ports, cmd_list, black_list):
    if nmap_type is None:
        return False
    nmap_net = "%s.0/24" % nmap_type
    nm = NmapDev(black_list)
    ssh_info, host_list, unknow_list = nm.nmap_sship(ports, nmap_net)
    can_login_list,  can_not_login_list = nm.try_login(sship_list, keyfile, cmdlist)
    print "Key login ...... ", can_login_list, can_not_login_list
    logger.info("Use key login:%s,%s"%(can_login_list,can_not_login_list))
    #email_message = u"可登录的服务器列表: %s \n 无法登录的服务器列表: %s \n 未知主机: %s \n" % (can_login_list, can_not_login_list, unknow_list)
    #email_sub = u"系统扫描结果"
    #receive_addr = s_emails
    #email_s = send_mail(receive_addr, email_sub, email_message)
    #email_s.send()
    if can_login_list:
        for item in can_login_list.keys():
            mathine_t = can_login_list[item][7] if can_login_list[item][7] else u"未知(需要安装dmidecode工具)"
            HostInfo.objects.update_or_create(ip=item,
                                                  hostname=can_login_list[item][0],
                                                  port=can_login_list[item][1],
                                                  user=can_login_list[item][2],
                                                  ssh_key=can_login_list[item][3],
                                                  #rsa_pass=can_login_list[item][3],
                                                  #ssh_type=can_login_list[item][4],
                                                  system_version=can_login_list[item][4],
                                                  sn=can_login_list[item][6],
                                                  mac=can_login_list[item][5],
                                                  host_type=mathine_t)
    return can_not_login_list

class NmapDev(object):
    def __init__(self, black_list=[]):
        self.black_list = []
        self.can_login_list = {}
        self.can_not_login_list = {}

    def nmap_allip(self, nmap_net):
        nm = nmap.PortScanner()
        nm.scan(hosts=nmap_net, arguments="-n -sP -PE")
        hostlist = nm.all_hosts()
        return hostlist

    def nmap_sship(self, ports, nmap_net):
        nm = nmap.PortScanner()
        nm.scan(hosts=nmap_net, arguments="-n -sP -PE")
        ssh_info = {}
        unknown_list = []
        tcp_all_ip = nm.all_hosts()
        host_list = []
        for ip in tcp_all_ip:
            if nm[ip]["status"]["state"] == "up":
                host_list.append(ip)
                for port in ports:
                    try:
                        print "Scan ip %s ...... Port %s" % (ip, port)
                        logger.info("Scan ip %s ...... Port %s" % (ip, port))
			try:
                            tm = telnetlib.Telnet(host=ip, port=port, timeout=3)
			except:
			    print "Scan ip %s ...... can not be login" % ip
			    continue
                        tm_res = tm.read_until("\n", timeout=5)
                        if tm_res:
                            if re.search("SSH", tm_res):
                                print ip
                                if ip not in self.black_list:
                                    ssh_info[ip] = port
                                    connect = "IP:%s Port:%s Server:%s" % (ip, port, tm_res)
                                    logger.info("IP:%s Port:%s Server:%s" % (ip, port, tm_res))
                                    print "IP:%s Port:%s Server:%s" % (ip, port, tm_res)
                            else:
                                if ip not in unknown_list and ip not in ssh_info.keys():
                                    unknown_list.append(ip)
                                logger.info("Telnet not ssh server:%s,%s,%s" % (ip, port, tm_res))
                                print "Open Res.....", ip, tm_res
                        else:
                            if ip not in unknown_list and ip not in ssh_info.keys():
                                unknown_list.append(ip)
                                logger.info("Telnet no data:%s, %s" % (ip, port))
                            print "Open ... ", ip
                    except EOFError as e:
                        if ip not in unknown_list and ip not in ssh_info.keys():
                            unknown_list.append(ip)
                        unknown_list.append(ip)
                        logger.exception("Telnet port EOFError:%s,%s,%s" % (ip, port, e))
                        print "Open....", ip, e
                if ip not in unknown_list and ip not in ssh_info.keys():
                    unknown_list.append(ip)
                        #logger.exception("Telnet port Exception:%s,%s,%s" % (ip, port, e))
                    print "error...", ip
        return ssh_info, host_list, list(set(unknown_list))

    def try_login(self, sship_list, keyfile, cmdlist):
        for ip, port in sship_list.items():
            print"try key login ...... ", ip, port
            logger.info("Try ssh idrsa key : %s,%s"%(ip,port))
            keyfile = "/home/raffaele/.ssh/id_rsa"
            if ip not in self.can_login_list.keys():
                logger.info("Try ssh id_rsa key: %s, %s, %s" % (ip, port, keyfile))
                print "Try ssh id_rsa key: %s, %s, %s" % (ip, port, keyfile)
                login_info = (ip, int(port), 'raffaele', keyfile)
                doobj = J_ssh_do()
                res = doobj.rsa_do(login_info, cmdlist)
                if res["status"] == "success":
                    sys_hostname = res["hostname"].replace('\n','')
                    system_info = getsysversion(res["cat /etc/issue |grep [0-9] || cat /etc/redhat-release |grep [0-9]"])
                    sys_mac = mac_trans(res["cat /sys/class/net/[^vftlsdb]*/address || esxcfg-vmknic -l|awk '{print $8}'|grep ':'"])
                    sys_sn = sn_trans(res["sudo dmidecode -s system-serial-number"].replace('\n',''))
                    machine_type = machine_type_trans(res["sudo dmidecode -s system-manufacturer"] + res["sudo dmidecode -s system-product-name"])
                    self.can_login_list[ip] = (sys_hostname, port, "raffaele", keyfile, system_info, sys_mac, sys_sn, machine_type)
                else:
                    if ip not in self.can_not_login_list.keys() and ip not in self.can_login_list.keys():
                        self.can_not_login_list[ip] = (port, keyfile)
        return self.can_login_list, self.can_not_login_list

nmap_net = myconf['hostinfo']['net'][0] + '.0/24'
dd = NmapDev()
print dd.nmap_allip(nmap_net)

sship_list = dd.nmap_sship([61318], nmap_net)[0]
keyfile = "/home/raffaele/.ssh/id_rsa"
cmdlist = myconf['hostinfo']['cmdlist']
print dd.try_login(sship_list, keyfile, cmdlist)

nmap_type = "192.168.37"
keyfile = "/home/raffaele/.ssh/id_rsa"
cmdlist = myconf['hostinfo']['cmdlist']
ports = [61318]
black_list = []
print nmap_begin(nmap_type, keyfile, ports, cmdlist, black_list)

#class Nmap_docker(NmapDev):
#    def __init__(self, d_cmds, ip_key_dic):
#        NmapDev.__init__(self):
#        self.docker_cmd_list = ["docker ps |awk -F '->' '{print $1}'|grep -v 'CONTAINER'|awk 'BEGIN{FS~/s+/;}{print $NF\" \"$1\" \"$2;}'|sed s/0.0.0.0://"]
#        self.d_cmds = d_cmds
#        self.p_docker_relate = {}
#        self.ip_key_dic = ip_key_dic
#
#    def do_namp(self, host_list):
#        ip_itmes = models.HostInfo.objects.filter(ip__in=host_list)
#        for ip_item in ip_items:
#            docker_dic = {}
#            login_info = [ip_item.ip, ip_item.port, ip_item.user, ip_item.ssh_key]
#            do_obj = J_ssh_do()
#            res = do_obj.rsa_do(login_info, self.docker_cmd_list)
#        port_list = res["docker ps |awk -F '->' '{print $1}'|grep -v 'CONTAINER'|awk 'BEGIN{FS~/s+/;}{print $NF\" \"$1\" \"$2;}'|sed s/0.0.0.0://"]
#        for d_item in port_list:
#            if d_item:
#                print ".................. d_item",  d_item
#                d_port, d_id, d_dn = re.split("\s+", d_item)[:3]
#                d_cid = d_id + d_dn
#                docker_dic[d_port] = d_cid
#        return docker_dic








