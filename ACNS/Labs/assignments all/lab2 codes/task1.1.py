#!/usr/bin/env python3
from scapy.all import *

print("SNIFFING OF PACKETS...")
def print_pkt(pkt):
    pkt.show()


pkt = sniff(iface=['br-81088c5890fc'], filter='icmp', prn=print_pkt)
