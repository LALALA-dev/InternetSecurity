from scapy.all import *

Qdsec = DNSQR(qname='vwxzy.example.com') #Query target name
dns = DNS(id=0xAAAA, qr=0, qdcount=1, ancount=0, nscount=0, arcount=0, qd=Qdsec) #construct DNS object
ip = IP(dst='10.9.0.53', src='10.9.0.5') #construct IP object # destination is 10.9.0.53 from 10.9.0.5
udp = UDP(dport=53, sport=3333, chksum=0) #construct UDP object # destination port is 53, source port is 5353
request = ip/udp/dns
#send(request)
with open('ip_req.bin','wb') as f:
    f.write(bytes(request))