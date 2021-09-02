import subprocess
import paramiko
from scp import SCPClient
from launch_threads import launch_threads
import util

def scp_files(name_and_ips):
    def send(name, ip):
        def exec(cmd, name, ip):
            stdin, stdout, stderr = ssh.exec_command(cmd.format(ip))
            err_message = stderr.read()
            if (err_message):
                print(err_message)
                print("Failed to execute command <{}> files to {} [{}]".format(cmd, ip, name))
                util.failexit()
            return stdout.read()
        print("Sending files to {} [{}]".format(ip, name))
        key = paramiko.ECDSAKey.from_private_key_file(util.get_path("terminal"))
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname = ip, username = "mith", pkey = key)
        exec("[ ! -d .cfg ] && mkdir .cfg", name, ip)
        with SCPClient(ssh.get_transport()) as scp:
            scp.put(util.get_path("data"), recursive = True, remote_path = "~/.cfg/")
            scp.put(util.get_path("remote_script"), recursive = True, remote_path = "~/.cfg/")
        outp = exec("python .cfg/remote_script/vm_cfg.py", name, ip)
        print(outp)
        ssh.close()

    def dispatch_param(idx):
        return name_and_ips[idx]
    launch_threads(function = send, dispatch_param = dispatch_param, num_threads = len(name_and_ips))

def remote_cfg(name_and_ips):
    #First scp all files and kick off self configuration script
    scp_files(name_and_ips)