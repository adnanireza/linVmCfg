from re import sub
import subprocess
import os.path
import os
import re
from shutil import copy, copyfile
import util


def host_bashrc_process(name_and_ips):
    f = open(util.get_path("bashrc.in.tmp"), "r")
    lines = f.readlines()
    f.close()
    for ip in name_and_ips:
        found = False
        for idx in range(len(lines)):
            if re.match(r'{}="\d+\.\d+\.\d+\.\d+'.format(ip[0]), lines[idx]):
                print(lines[idx])
                lines[idx] = re.sub(r'\d+\.\d+\.\d+\.\d+', ip[1], lines[idx])
                print(lines[idx])
                found = True
                break
        if not found:
            lines.append('\r\n{}="{}"'.format(ip[0], ip[1]))
    f = open(util.get_path("bashrc.out.tmp"), "w")
    f.writelines(lines)
    f.close()

def host_bashrc(name_and_ips):
    # Copy (create if doesn't exist) bashrc file so python can modify
    run = subprocess.run("bash {} {} {}".format(util.get_path("copy_file.sh"), util.get_path("host_cfg_DIR"), "bashrc"),\
        universal_newlines = True,\
        stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    if run.returncode or run.stderr:
        print(run.stderr)
        util.failexit()

    # Process bashrc file
    host_bashrc_process(name_and_ips)

    # Copy bashrc back to home
    run = subprocess.run("bash {} {} {}".format(util.get_path("copy_file_back.sh"), util.get_path("host_cfg_DIR"), "bashrc"),\
        universal_newlines = True,\
        stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    if run.returncode or run.stderr:
        print(run.stderr)
        util.failexit()

    # Delete temporary bashrc files
    os.remove(util.get_path("bashrc.in.tmp"))
    os.remove(util.get_path("bashrc.out.tmp"))

def host_vimrc_process():
    f = open(util.get_path("vimrc.in.tmp"), "r")
    vimrc_lines = f.readlines()
    f.close()
    f = open(util.get_path("vimrc.txt"), "r")
    new_lines = f.readlines()
    f.close()
    for new_line in new_lines:
        found = False
        for idx in range(len(vimrc_lines)):
            if new_line == vimrc_lines[idx]:
                found = True
                break
        if not found:
            vimrc_lines.append(new_line)
    f = open(util.get_path("vimrc.out.tmp"), "w")
    f.writelines(vimrc_lines)
    f.close()

def host_vimrc():
    # Copy (create if doesn't exist) vimrc file so python can modify
    run = subprocess.run("bash {} {} {}".format(util.get_path("copy_file.sh"), util.get_path("host_cfg_DIR"), "vimrc"),\
        universal_newlines = True,\
        stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    if run.returncode or run.stderr:
        print(run.stderr)
        util.failexit()
    
    # Update vimrc if needed
    host_vimrc_process()

    # Copy vimrc back to home
    run = subprocess.run("bash {} {} {}".format(util.get_path("copy_file_back.sh"), util.get_path("host_cfg_DIR"), "vimrc"),\
        universal_newlines = True,\
        stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    if run.returncode or run.stderr:
        print(run.stderr)
        util.failexit()

    # Delete temporary vimrc files
    os.remove(util.get_path("vimrc.in.tmp"))
    os.remove(util.get_path("vimrc.out.tmp"))

def sshkey(name_and_ips):
    # Generate ssh key if needed
    run = subprocess.run("bash {}".format(util.get_path("sshkey_gen.sh")),\
        universal_newlines = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    if run.returncode or run.stderr:
        print(run.stderr)
        util.failexit()
    
    # Send ssh key
    for ip in name_and_ips:
        run = subprocess.run("bash {} {} {}".format(util.get_path("sshkey_send.sh"), ip[1],\
            util.conv_path_win2lin(util.get_path("session.pub"))), universal_newlines = True)
        if run.returncode:
            print(run.stderr)
            util.failexit()
    # print("Attempted to send ssh key. Press a key to continue or CTRL+C to exit...")
    # input()

def host_cfg(name_and_ips):
    host_bashrc(name_and_ips)
    host_vimrc()
    sshkey(name_and_ips)