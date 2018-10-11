#!/usr/bin/evn python

import subprocess
import optparse
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="This helps select the interface")
    parser.add_option("-m", "--mac", dest="new_mac", help="This helps set new mac address")
    (options, arguments)= parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify the interface, use --help for futher help")
    elif not options.new_mac:
        parser.error("[-]Please specify mac address, use --help for futher help")
    return options

def change_mac(interface, new_mac):
    print("Changing mac address of " + interface + " to" + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options=get_arguments()
change_mac(options.interface, options.new_mac)
