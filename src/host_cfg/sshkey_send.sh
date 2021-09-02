#
# bash {} {} {}".format(util.get_path("sshkey_send.sh"), ip[1], util.conv_path_win2lin(util.get_path("session.pub"))
#                                           $0             $1                                             $2
#

# send terminal ssh key
ssh-copy-id mith@$1

# send session ssh key
ssh-copy-id -i $2 mith@$1