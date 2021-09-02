from remote_script import mylib

name_and_ips = mylib.getips()
print(name_and_ips)
mylib.bashrc(name_and_ips)
mylib.vimrc()
mylib.ssh_key()