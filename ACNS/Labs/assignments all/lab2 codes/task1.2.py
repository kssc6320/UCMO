#!/usr/bin/env python3
from scapy.all import *
from scapy.layers.inet import IP, ICMP

print("SENDING SPOOFED ICMP PACKET....")
ip = IP(src='8.8.8.8', dst='10.0.2.3')
icmp = ICMP()
pkt = ip / icmp
pkt.show()
send(pkt, verbose=0)
ls(IP)
