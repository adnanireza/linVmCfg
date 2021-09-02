import subprocess

def bash_no_log(cmd):
    run = subprocess.run(cmd, universal_newlines = True, shell = True,\
        stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    if run.returncode or run.stderr:
        print(run.stderr)
        print("Exiting...")
        exit(-1)
    return run.stdout

my_ip = bash_no_log(r"hostname -I | awk '{print $1}'").strip("\n")
my_name = bash_no_log(r'hostname').strip("\n")
