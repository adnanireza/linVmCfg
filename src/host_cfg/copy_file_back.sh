#
# "bash {} {} {}".format(copy_file_back_sh, host_cfg_dir "bashrc")
#                              $0               $1          $2
#
FILE=".$2"
cd
cp $1\\$2.out.tmp $FILE
dos2unix $FILE
