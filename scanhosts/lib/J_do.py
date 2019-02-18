#!/usr/bin/python
#!-*- code: utf8 -*-

import logging
import paramiko
import yaml
import traceback

myconf = yaml.load(file('../../conf/scanhosts.yaml'))
logger = logging.getLogger("django")

class J_ssh_do(object):
    def __init__(self):
        self.result = {}

    def get_ip(self, login_info):
        net = "%s.0/24" % login_info[0]
        ports = login_info[1]
        nm = nmap.PortScanner()
        nm.scan(hosts=net, arguments="-n -sP -PE")
        ip_list = nm.all_hosts()
        ipinfo = []
        for ip in ip_list:
            for port in ports:
                try:
                    tm = telnetlib.Telnet(host=ip, port=port, timeout=4)
                    result = tm.read_until("\n", timeout=4)
                    if re.search('SSH', result):
                        logger.info("%s is alive!!" % ip)
                        ipinfo.append(ip)
                    else:
                        continue
                except:
                    logger.info("%s can not be login !!" % ip)
        return ipinfo

    def rsa_do(self, login_info, cmdlist):
        try:
            jssh = paramiko.SSHClient()
            jssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            key = paramiko.RSAKey.from_private_key_file(login_info[3])
            jssh.connect(login_info[0], login_info[1], login_info[2], pkey=key, timeout=3)
            self.result["status"] = "success"
            for cmd in cmdlist:
                stdin, stdout, stderr = jssh.exec_command(cmd)
                std_res = stdout.read()
                self.result[cmd] = std_res
        except Exception as e:
            logger.exception("Use rsa key ssh login exception:%s, %s" % (e, login_info))
            self.result["status"] = "Failed"
            self.result["res"] = e
        return self.result




