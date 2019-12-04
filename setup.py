
# Setup and activation of Termux-Lock

import os,sys

os.chdir('/data/data/com.termux/files/usr/etc')

opr = open('bash.bashrc','a')
opr.write("\nalias usr='python /data/data/com.termux/files/home/MyRepo/Termux-Lock.py -l' \n")
opr.write('figlet -c -k -f slant Termux-Lock|lolcat;usr \n')
opr.close()

os.system('apt install figlet')
os.system('pip install stdiomask')
