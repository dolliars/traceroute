import sys
from scapy.all import sr1, IP, ICMP

x = 30

for i in range(x):
    pkt=IP(ttl=x)
    pkt.dst="8.8.8.8"
    sr1(pkt)
