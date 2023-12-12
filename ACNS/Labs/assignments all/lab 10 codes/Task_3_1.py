#!/bin/bash

ssh -w 0:0 root@192.168.20.99 \
    -o "PermitLocalCommand=yes" \
    -o "LocalCommand= ip addr add 192.168.53.88/24 dev tun0 && ip link set tun0 up \
    && ip route replace 192.168.20.0/24 dev tun0 \
    && ip route add 192.168.20.99/32 via 10.8.0.11" \
    -o "RemoteCommand=ip addr add 192.168.53.99/24 dev tun0 && ip link set tun0 up"
# on Al, A2 add
# ip route replace 192.168.20.0/24 via 10.8.0.99
# on B1, B2 add
# ip route add 10.8.0.0//24 via 192.168.20.99
