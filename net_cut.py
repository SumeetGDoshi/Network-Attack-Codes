#! /usr/bin/env python

import netfilterqueue
import scapy.all as scapy
def process_packet(packet):
    scapy_packet = scapy.IP(packet)
    print(scapy_packet)
    packet.accept()
    # return packet

queue = netfilterqueue.NetfilterQueue()
queue.bind(3, process_packet)
queue.run()

# p_packets = process_packet(packet)
# print(p_packets)

#echo 1 > /proc/sys/net/ipv4# /ip_forward