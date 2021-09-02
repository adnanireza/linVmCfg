import subprocess
import paramiko
from remote_script.init import *
from remote_script.log import *

def bash(cmd):
    log_info("Sending command: <{}>".format(cmd))
    run = subprocess.run(cmd, universal_newlines = True, shell = True,\
        stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    if run.returncode or run.stderr:
        print(run.stderr)
        error_exit()
    log_debug("command output: " + run.stdout)
    return run.stdout

def ssh_open(ip, passwd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname = ip, username = "mith", password = passwd)
    except paramiko.ssh_exception.AuthenticationException as err:
        log_error("Authentication failure")
        log_error(err)
        error_exit()
    return ssh

def ssh_exec(cmd, ssh):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    err_message = stderr.read()
    if (err_message):
        log_error("Output:<<<")
        log_error(stdout.read().decode("ascii"))
        log_error(">>>:Output")
        log_error("ERROR:<<<".format(my_ip, my_name))
        log_error(err_message.decode("ascii"))
        log_error(">>>:ERROR")
        log_error("Failed to execute command <{}> files to {} [{}]".format(cmd, my_ip, my_name))
        error_exit()
    return stdout.read().decode("ascii")

def ssh_close(ssh):
    ssh.close()