#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This just scans IP addresses and stores which ones are responsive 
and which ones are not in an array

@author: CyberTools101
"""
import ipaddress
import os
from multiprocessing.pool import ThreadPool as Pool


#Arrays to hold both responsive and unresposive IPs
live = [] 
dead = []

#The ip address and subnet I am interested in scanning
starting_ip = "10.0.0.0"
subnet = "24"

#Create a iterable list of IPs
ips = [str(hostname) for hostname in ipaddress.IPv4Network(starting_ip + '/' + subnet)]

#Use this as an output to let me know how many have been pinged thus far
def keep_track(ip):   
    if ip == starting_ip:
        print("Started program")
    elif ips.index(ip)/(len(ips) - 1) == 1:
        print("Pinged 100% of IP range\nAwaiting responses")
    elif ips.index(ip)/len(ips) == .25:
        print("Pinged 25% of IP range")
    elif ips.index(ip)/len(ips) == .50:
        print("Pinged 50% of IP range")
    elif ips.index(ip)/len(ips) == .75:
        print("Pinged 75% of IP range")
    ping_ip(ip)
    
#Ping the ip address, just send one packet and move on
def ping_ip(ip): 
    response = os.system("ping -c 1 " + ip)
    
    #Add it to the proper array
    if response == 0:
      live.append(ip)
    else: 
      dead.append(ip)
   
#Start the program
def main():
    
    #Gotta pool it, cause scanning one by one will take too long
    result = Pool().map_async(keep_track, ips)
    result.wait()
    
    #check to make sure we have all the results we are interested in
    if len(live) + len(dead) == len(ips):
        print("Results finised.")
    
    #print the responsive IPs
    print(live)
        
main();

