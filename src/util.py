import os.path

def failexit(exit_code = -1):
    print("Exiting...")
    exit(exit_code)

def get_rootdir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

def get_path(item):
    if item == "ips.txt":
        return os.path.join(get_rootdir(), "data", "ips.txt")
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
    
    print("Can't find path for " + item)
    failexit()