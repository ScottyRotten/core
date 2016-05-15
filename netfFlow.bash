SRC IP = tcpdump -n -r first_contact.pcap | awk '{print $3}' | sort | uniq -c

DST IP = tcpdump -n -r first_contact.pcap | awk '{print $5}' | sort | uniq -c

SRC AND DST IP = tcpdump -m -r first_contact.pcap | awk '{print $3, $5}' | sort | uniq -c

RECORD AND SAVE TO TIMESTAMPED FILE EVERY 5 MINUTES - tcpdump -G 300 -w %T

a 