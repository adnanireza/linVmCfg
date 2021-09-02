import os.path
import sys
from remote_script import tool

pubkey = "{} {}".format(sys.argv[1], sys.argv[2])

print(pubkey)
keysfile = "/home/mith/.ssh/authorized_keys"
if not os.path.isfile(keysfile):
    tool.bash('echo {} > keysfile')
    exit(0) # All done!

f = open(keysfile, "r")
lines = f.readlines()
f.close()

for line in lines:
    if pubkey == line:
        found = True
        exit(0) # Nothing more needs to be done!

lines.append("\n" + pubkey)

f = open(keysfile, "w")
f.writelines(lines)
f.close()
