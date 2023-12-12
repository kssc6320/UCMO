#!/bin/bash
ssh -w 0:0 root@10.8.0.99 \
    -o "PermitLocalCommand=yes" \
    -o "LocalCommand= ip addr add 192.168.53.88/24 dev tun0 && ip link set tun0 up \
    && ip route add 93.184.216.0/24 dev tun0 \
    && iptables -t nat -A POSTROUTING -j MASQUERADE -o tun0" \
    -o "RemoteCommand=ip addr add 192.168.53.99/24 dev tun0 && ip link set tun0 up \
    && iptables -t nat -A POSTROUTING -j MASQUERADE -o eth0"
# on B1 B2 add
# ip route add 93.184.216.0/24 via 192.168.20.99
