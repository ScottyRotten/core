#!/usr/bin/python

"""
    Copyright (C) 2016 @scottyrotten

    Recon - A post exploitation enumeration tool for linux/unix devices
    that have Python 2.* installed.
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    For more see the file 'LICENSE' for copying permission.
"""

__author__ = "scottyrotten"
__copyright__ = "Copyright (c) 2016 @scottyrotten"
__credits__ = ["scottyrotten"]
__license__ = "GPLv3"
__version__ = ".1"
__maintainer__ = "scottyrotten"

##########################################
# Libraries

import argparse
import os
import platform

##########################################

# parse arguements from command line/help file documentation

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', help='directory to use', action='store')
args = parser.parse_args()

# Setup

OSTYPE = platform.linux_distribution()
OUTFILE = open(args.directory, 'w+')
SYSFILES = [
    '/etc/issue',
    #'/etc/*-release'
    #'/etc/sysconfig/network',
    '/etc/resolv.conf',
    '/etc/fstab',
    '/etc/passwd',
    #'/etc/shadow',
    '/etc/group',
    #'/etc/sudoers',
]

'''
EXEC = [
    '/bin/uname -r',
    'mount | column -t',
    #sticky bit files
    '/usr/bin/find / -perm -g=s -o -perm -4000 ! type l -maxdepth 3 -exec ls -ld {} \; 2>/dev/null',
    #world directories
    '/usr/bin/find / -perm 222 -type d 2>/dev/null',
    #world writeable files
    '/usr/bin/find / -perm 0777 -type f 2>/dev/null'
    '/usr/bin/find / -user $(whoami) 2>/dev/null',
    '/usr/bin/w',
    '/usr/bin/'last',
    '/usr/bin/ps -ef | grep root'
]
'''
#OUTPUT FILE COLORS

ENDC = '\033[0m'
HEADER = '\033[95m'

#Determine if Debian, RHEL

if OSTYPE[0] == 'Ubuntu':
    print "Ubuntu"
else:
    print "RHEL"

# Define function to read files and write to output

def fileRead(file_list):
    for i in file_list:
        with open(i, 'r') as file:
            OUTFILE.write(HEADER+ 25 * '#' +ENDC)
            OUTFILE.write('\n\n')
            OUTFILE.write(file.read())

fileRead(SYSFILES)

# List directories

for root, dirs, filenames in os.walk('/home/'):
    for name in filenames:
        OUTFILE.write(os.path.join(root, name))
    for name in dirs:
        OUTFILE.write(os.path.join(root, name))


# Exfil collected data (zip up, SCP back to remote host)

# Cleanup log files to remove traces of recon from system

OUTFILE.close()
