import sys
from scapy.all import sr1, IP, ICMP
x = 30
for i in range(x):
    pkt=IP(ttl=x)
    pkt.dst="8.8.8.8"
    ans = sr1(pkt/ICMP())
    if ans is None:
        break
    elif ans.type == 3:
        print ("Done!", ans.src)
        break
    else:
        print ("Hop %d: " % i , ans.src)
