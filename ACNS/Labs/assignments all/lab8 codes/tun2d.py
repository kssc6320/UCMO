#!/usr/bin/env python3

import fcntl

from scapy.all import *

TUNSETIFF = 0x400454ca
IFF_TUN = 0x0001
IFF_TAP = 0x0002
IFF_NO_PI = 0x1000

# Create the tun interface
tun = os.open("/dev/net/tun", os.O_RDWR)
ifr = struct.pack('16sH', b'subhatun%d', IFF_TUN | IFF_NO_PI)
ifname_bytes = fcntl.ioctl(tun, TUNSETIFF, ifr)

# Get the interface name
ifname = ifname_bytes.decode('UTF-8')[:16].strip("\x00")
print("Interface Name: {}".format(ifname))

os.system("ip addr add 192.168.157.140/24 dev {}".format(ifname))
os.system("ip link set dev {} up".format(ifname))

while True:
    # Get a packet from the tun interface
    packet = os.read(tun, 2048)
    if True:
        ip = IP(packet)
        print(ip.summary())
        if ICMP in ip and ip[ICMP].type == 8:
            newip = IP(src=ip.dst, dst=ip.src)
            icmp = ICMP(type=0, id=ip[ICMP].id, seq=ip[ICMP].seq)
            newpkt = newip / icmp / ip[Raw].load
            os.write(tun, bytes(newpkt))
