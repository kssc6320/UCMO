#!/usr/bin/python3
from scapy.all import *

print("SNIFFING PACKETS...")


def print_pkt(pkt):
    pkt.show()


pkt = sniff(filter='src net 128.230.0.0/16', prn=print_pkt)
