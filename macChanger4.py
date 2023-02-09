#!/usr/bin/env python3

# FUNCTIONS

import subprocess
import optparse


# def function for arguments
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    # Custom names which are clear were "options "arguments" and "parser"
    return parser.parse_args()


# def function for new mac address
def change_mac(interface, new_mac):
    print("[+] Changing Mac Address for " + interface + " to " + new_mac + "\n")

    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    subprocess.call(["ifconfig"])

    print(f"The MAC ADDRESS has now been changed to {new_mac}")

(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)
