#
# "bash {} {} {}".format(copy_file_sh, host_cfg_dir "bashrc")
#                           $0              $1          $2
#
FILE=".$2"
cd
if [ ! -f $FILE ]; then
    echo "${FILE} does not exist. Creating..."
    touch $FILE
fi
cp $FILE $1\\$2.in.tmp
