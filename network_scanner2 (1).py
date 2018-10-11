import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    # print(arp_request.summary())
    # scapy.ls(scapy.ARP()) this is to see which parameters does scapy.ARP() accepts and how
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # print(broadcast.summary())
    arp_request_broadcast = broadcast / arp_request
    print(arp_request_broadcast.summary())
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]
    # print(answered_list.summary())
    for element_is_variable in answered_list:
        print("The target ip Address is", element_is_variable[1].psrc)
        print("The target Mac Address is", element_is_variable[1].hwsrc)

        print("--------------------------------------------------")



scan("10.0.2.1/24")