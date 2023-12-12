#!/usr/bin/env python3

import fcntl

from scapy.all import *

TUNSETIFF = 0x400454ca
IFF_TUN = 0x0001
IFF_TAP = 0x0002
IFF_NO_PI = 0x1000

# Create the tun interface
tap = os.open("/dev/net/tun", os.O_RDWR)
ifr = struct.pack('16sH', b'subhatap%d', IFF_TAP | IFF_NO_PI)
ifname_bytes = fcntl.ioctl(tap, TUNSETIFF, ifr)

# Get the interface name
ifname = ifname_bytes.decode('UTF-8')[:16].strip("\x00")
print("Interface Name: {}".format(ifname))

os.system("ip addr add 192.168.53.99/24 dev {}".format(ifname))
os.system("ip link set dev {} up".format(ifname))

while True:
    # Get a packet from the tun interface
    packet = os.read(tap, 2048)
    if True:
        ether = Ether(packet)
        arp = ether[ARP]
        ether.show()
        if ARP in ether and ether[ARP].op == 1:
            newarp = ARP(psrc=arp.pdst, hwsrc='aa:bb:cc:dd:ee:ff',
                         pdst=arp.psrc, hwdst=ether.src, op=2)
            newether = Ether(src='aa:bb:cc:dd:ee:ff', dst=ether.src)
            newpkt = newether / newarp
            print("*** Fake response: {}".format(newpkt.summary()))
            os.write(tap, bytes(newpkt))
