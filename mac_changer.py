#!/usr/bin/env python

import subprocess
import optparse

def getmac(interface):
  try:
    mac = open('/sys/class/net/'+interface+'/address').readline()
    print("")
    print("[+] The current MAC address is " +mac)
  except:
    print("[-] Something went wrong")


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Select an interface")
    parser.add_option("-m", "--mac", dest="new_mac", help="Set MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    print("")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
getmac(options.interface)
change_mac(options.interface, options.new_mac)
