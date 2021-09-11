import getpass
from os import name
import paramiko
from scp import SCPClient
from common.launch_threads import launch_threads
import util

def exec(cmd, name, ip, ssh):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    err_message = stderr.read()
    if (err_message):
        print("Output[{}({})]:<<<".format(ip, name))
        print(stdout.read().decode("ascii"))
        print(">>>:Output")
        print("ERROR[{}({})]:<<<".format(ip, name))
        print(err_message.decode("ascii"))
        print(">>>:ERROR")
        print("Failed to execute command <{}> files to {} [{}]".format(cmd, ip, name))
        util.failexit()
    return stdout.read().decode("ascii")
def ssh_open(ip):
    key = paramiko.ECDSAKey.from_private_key_file(util.get_path("terminal"))
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname = ip, username = "mith", pkey = key)
    return ssh

def ssh_close(ssh):
    ssh.close()

def remote_cfg(name_and_ips):
    def send(name, ip):
        print("Sending files to {} [{}]".format(ip, name))
        ssh = ssh_open(ip)
        exec("[ ! -d .cfg ] && mkdir .cfg", name, ip, ssh)
        with SCPClient(ssh.get_transport()) as scp:
            scp.put(util.get_path("data"), recursive = True, remote_path = "~/.cfg/")
            scp.put(util.get_path("ips.txt"), remote_path = "~/.cfg/data")
            scp.put(util.get_path("common"), recursive = True, remote_path = "~/.cfg/")
            scp.put(util.get_path("remote_script"), recursive = True, remote_path = "~/.cfg/")
            scp.put(util.get_path("vm_cfg_1.py"), remote_path = "~/.cfg/")
            scp.put(util.get_path("vm_cfg_2.py"), remote_path = "~/.cfg/")
            scp.put(util.get_path("remote_vm.py"), remote_path = "~/.cfg/")
        exec("chmod +x ~/.cfg/remote_script/configure.sh", name, ip, ssh)
        outp = exec("python3 .cfg/vm_cfg_1.py", name, ip, ssh)
        print("Output[{}({})]:<<<".format(ip, name))
        print(outp)
        print(">>>:Output")        
        ssh_close(ssh)

    def dispatch_param_1(idx):
        return (name_and_ips[idx][0], name_and_ips[idx][1])

    # First send all files, and start kick off the first script
    launch_threads(function = send, dispatch_param = dispatch_param_1, num_threads = len(name_and_ips))

    # Finally take password and kick off the second script
    print("Please enter VM password: ")
    passwd = getpass.getpass()

    def dispatch_param_2(idx):
        return (name_and_ips[idx][0], name_and_ips[idx][1], passwd)

    def run(name, ip, passwd):
        ssh = ssh_open(ip)
        print("Kicking off second script to {} [{}]".format(ip, name))
        outp = exec("python3 .cfg/vm_cfg_2.py {}".format(passwd), name, ip, ssh)
        print("Output[{}({})]:<<<".format(ip, name))
        print(outp)
        print(">>>:Output")        
        ssh_close(ssh)

    launch_threads(function = run, dispatch_param = dispatch_param_2, num_threads = len(name_and_ips))

    print("If no  e r r o r s  printed, most likely all VMs configured!!?")
    print("List of vms: ")
    print(name_and_ips)