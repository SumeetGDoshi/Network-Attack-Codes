#!/usr/bin/evn python

import subprocess

interface= raw_input("New interface>")

new_mac=raw_input("new mac>")
print("Changing mac address of " + interface + " to"+ new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
