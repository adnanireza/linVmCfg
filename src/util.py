import os.path
import re

def failexit(exit_code = -1):
    print("Exiting...")
    exit(exit_code)

def get_rootdir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

def conv_path_win2lin(winpath):
    "Applies for mobaxterm terminal only"
    # print("WIN: " + winpath)
    linpath = re.sub(r":", "", winpath)
    linpath = r"/drives/" + re.sub(r"\\", r"/", linpath)
    return linpath.lower()
    # print("LIN: " + linpath)

def get_path(item):
    if item == "ips.txt":
        return os.path.join("C:\\", "Mithun", "computers", "linux", "secrets", "vm_ips", "ips.txt")
    if item == "session":
        return os.path.join("C:\\", "Mithun", "computers", "linux", "secrets", "mobaxterm_session_keys", "session")
    if item == "session.pub":
        return os.path.join("C:\\", "Mithun", "computers", "linux", "secrets", "mobaxterm_session_keys", "session.pub")
    if item == "terminal":
        return os.path.join("C:\\", "Mithun", "computers", "linux", "secrets", "mobaxterm_terminal_keys", "terminal")
    if item == "terminal.pub":
        return os.path.join("C:\\", "Mithun", "computers", "linux", "secrets", "mobaxterm_terminal_keys", "terminal.pub")
    if item == "data":
        return os.path.join(get_rootdir(), "data")
    elif item == "remote_script":
        return os.path.join(get_rootdir(), "src", "remote_script")
    elif item == "vm_cfg_1.py":
        return os.path.join(get_rootdir(), "src", "remote_script", "vm_cfg_1.py")
    elif item == "vm_cfg_2.py":
        return os.path.join(get_rootdir(), "src", "remote_script", "vm_cfg_2.py")
    elif item == "remote_vm.py":
        return os.path.join(get_rootdir(), "src", "remote_script", "remote_vm.py")
    elif item == "vimrc.txt":
        return os.path.join(get_rootdir(), "data", "vimrc.txt")
    elif item == "host_cfg_DIR":
        return os.path.join(get_rootdir(), "src", "host_cfg")
    elif item == "bashrc.in.tmp":
        return os.path.join(get_rootdir(), "src", "host_cfg", "bashrc.in.tmp")
    elif item == "bashrc.out.tmp":
        return os.path.join(get_rootdir(), "src", "host_cfg", "bashrc.out.tmp")
    elif item == "vimrc.in.tmp":
        return os.path.join(get_rootdir(), "src", "host_cfg", "vimrc.in.tmp")
    elif item == "vimrc.out.tmp":
        return os.path.join(get_rootdir(), "src", "host_cfg", "vimrc.out.tmp")
    elif item == "host_cfg.sh":
        return os.path.join(get_rootdir(), "src", "host_cfg", "host_cfg.sh")
    elif item == "copy_file.sh":
        return os.path.join(get_rootdir(), "src", "host_cfg", "copy_file.sh")
    elif item == "copy_file_back.sh":
        return os.path.join(get_rootdir(), "src", "host_cfg", "copy_file_back.sh")
    elif item == "sshkey_gen.sh":
        return os.path.join(get_rootdir(), "src", "host_cfg", "sshkey_gen.sh")
    elif item == "sshkey_send.sh":
        return os.path.join(get_rootdir(), "src", "host_cfg", "sshkey_send.sh")
    elif item == "my_scp.sh":
        return os.path.join(get_rootdir(), "src", "remote_cfg", "my_scp.sh")
    elif item == "common":
        return os.path.join(get_rootdir(), "src", "common")

    import traceback
    print(traceback.extract_stack(None, 2))
    print("Can't find path for " + item)
    failexit()