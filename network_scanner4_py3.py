#! /usr/bin/evn python

import scapy.all as scapy
import argparse
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="ip", help="This helps set ip of target")

    (options, arguments)= parser.parse_args()
    if not options.ip:
        parser.error("[-] Please specify the ip, use --help for futher help")

    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    # print(arp_request.summary())
    # scapy.ls(scapy.ARP()) this is to see which parameters does scapy.ARP() accepts and how
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # print(broadcast.summary())
    arp_request_broadcast = broadcast / arp_request
    # print(arp_request_broadcast.summary())
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    # print(answered_list.summary())

    client_list=[]
    for element_is_variable in answered_list:
        client_dict={"ip": element_is_variable[1].psrc, "mac": element_is_variable[1].hwsrc}
        client_list.append(client_dict)
        # print(element_is_variable[1].psrc +"\t\t" + element_is_variable[1].hwsrc)
    return client_list

def print_result(result_list):
    print("IP \t\t\t MAC ADDRESS\n------------------------------------------------------------------")
    for client in result_list:
        print(client["ip"] +"\t\t"+ client["mac"])

options=get_arguments()
scan_result=scan(options.ip)
print_result(scan_result)