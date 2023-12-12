#!/usr/bin/python3

print("SNIFFING OF PACKETS...")





def print_pkt(pkt):

        pkt.show()





        pkt = sniff(iface=['br-81088c5890fc'], filter='tcp && src host 10.9.0.5 && dst port 23', prn=print_pkt)
