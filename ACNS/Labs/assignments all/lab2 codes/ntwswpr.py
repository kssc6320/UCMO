#!/usr/bin/env python3
from scapy.all import *

import os

IP = input("[+] Enter the Host IP Address:\t")
print("[+] Starting for network Sweeper on " + IP)
dot = IP.rfind(".")
IP = IP[0:dot + 1]
for i in range(1, 255):
    host = IP + str(i)
    response = os.system("ping -c 1 -w 1 " + host + " >/dev/null")

    if response == 0:
        print(host + " IP address is up")
    else:
        print(host + " IP address is down")