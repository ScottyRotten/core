#!/usr/python

import subprocess

pcap = subprocess.call(["tcpdump", "-r", "/Users/helloroot/Documents/laughing-spork/first_contact.pcap"])
