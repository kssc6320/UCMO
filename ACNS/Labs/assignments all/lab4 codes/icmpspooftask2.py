#!/usr/bin/python3

from scapy.all import *
from scapy.layers.inet import *

src_ip = '4.3.2.1'
dst_ip = '192.168.60.5'

pkt = IP(src=src_ip, dst=dst_ip)/ICMP()
print(pkt.summary())
send(pkt, verbose=0)
