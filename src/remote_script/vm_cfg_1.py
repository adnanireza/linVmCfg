from remote_script import mylib

# Get name and ips from text file
name_and_ips = mylib.getips()

# Configure bashrc and vimrc files
mylib.bashrc(name_and_ips)
mylib.vimrc()

# Generate ssh key if needed
mylib.gen_key()
