#!/usr/bin/env python3

import subprocess

# VARIABLES
interface = input("Which interface would you like to change? eth0 or eth1: ")
new_mac = input("Enter the mac address you want. example 00:00:00:00:00:00: ")

print("[+] Changing Mac Address for " + interface + " to " + new_mac + "\n")

subprocess.call(["sudo", "ifconfig", interface, "down"])
subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["sudo", "ifconfig", interface, "up"])
subprocess.call(["ifconfig"])

print(f"The MAC ADDRESS has now been changed to {new_mac}")



