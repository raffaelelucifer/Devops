#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
os.environ["DJANGO_SETTINGS_MODULE"] = 'Devops.settings'
import django
import time
django.setup()
import paramiko
from scanhosts.models import DockerInfo

class nmap_docker(object):
    def __init__(self):
        pass

    def get_docker_hostlist(self, hostlist, *args, **kwargs):
        jssh = paramiko.SSHClient()
        jssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        key = paramiko.RSAKey.from_private_key_file('/home/raffaele/.ssh/id_rsa')
        docker_hostlist = []
        for host in hostlist:
            jssh.connect(host, 61318, "raffaele", pkey=key)
            try:
                stdin, stdout, stderr = jssh.exec_command("sudo docker ps |wc -l")
                docker_info = stdout.read()
                if docker_info:
                    docker_hostlist.append(host)
                    print "There is docker service in %s " % host
                    continue
            except:
                print "There is no docker service in %s " % host
                continue
        return docker_hostlist

    def nmap_docker(self):
        #hostlist = models.HostInfo.objects.all()
        #hostarray = []
        #for host in hostlist.ip:
        #    hostarray.append(host.ip)
        hostarray = ["192.168.37.143"]
        docker_hostlist = self.get_docker_hostlist(hostarray)
        jssh = paramiko.SSHClient()
        jssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        key = paramiko.RSAKey.from_private_key_file('/home/raffaele/.ssh/id_rsa')
        dockerlist = {}
        for docker_host in docker_hostlist:
            jssh.connect(docker_host, 61318, 'raffaele', pkey=key)
            stdin, stdout, stderr = jssh.exec_command("sudo docker ps |awk '{print $1}' |grep -v 'CONTAINER'")
            res = stdout.read()
            res2 = res.split("\n")
            res2.pop()
            dockerlist[docker_host] = res2
        return dockerlist

    def collect_docker_info(self, *args, **kwargs):
        dockerlist = self.nmap_docker()
        docker_cmd = {}
        docker_cmd_f = {}
        for host in dockerlist.keys():
            #login_info = [host, 61318, 'raffaele', '/home/raffaele/.ssh/id_rsa']
            #obj = J_ssh_do.rsa_do
            #obj.rsa_do(login_info)
            jssh = paramiko.SSHClient()
            jssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            key = paramiko.RSAKey.from_private_key_file('/home/raffaele/.ssh/id_rsa')
            jssh.connect(host, 61318, 'raffaele', pkey=key)
            name_stdin, name_stdout, name_stderr = jssh.exec_command("sudo hostname")
            d_hostname = name_stdout.read()
            for id in dockerlist[host]:
                port_stdin, port_stdout, port_stderr = jssh.exec_command("sudo docker ps |grep -v CONTAINER |grep %s |awk -F '->' '{print $1}' |awk '{print $NF}' |sed s/0.0.0.0://" % id)
                docker_port = port_stdout.read()
                print docker_port
                service_stdin, service_stdout, service_stderr = jssh.exec_command("sudo docker ps |grep -v CONTAINER |grep %s |awk '{print $2}' |awk -F '/' '{print $NF}'" % id)
                docker_service = service_stdout.read()
                print docker_service
                if docker_port.replace('\n','').isdigit():
                    pass
                else:
                    docker_port = None
                docker_cmd.update({id:[docker_port, docker_service]})
                dd = DockerInfo.objects.create(hostname=d_hostname, ip=host, docker_id=id, port=docker_port, service=docker_service)
                dd.save()
            docker_cmd_f[host] = docker_cmd
        return docker_cmd_f

dd = nmap_docker()
print dd.collect_docker_info()






