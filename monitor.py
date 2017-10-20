#!/usr/bin/env python
#-*- coding: utf-8 -*-

import numpy as np
import Queue
import threading
import time
import datetime

from serial import Serial

debug=False

## Serial port simulation ##
from Rat import Rat

## Define some Serial read functions
queue = Queue.Queue(0)

def get_all_queue_result(queue):

    result_list = []
    while not queue.empty():
        result_list.append(queue.get())

    return result_list

def serial_read(s, q, sid):
    while True:
        line = s.readline().strip()
        if debug==True:
            print time.strftime("%Y-%m-%d %H:%M:%S"), sid, line
        else:
            out = ' '.join([time.strftime("%Y-%m-%d %H:%M:%S"), rats[line], sid])
            q.put(out)
            print out

ports = {'P1': '/dev/ttyUSB0',
         'P2': '/dev/ttyUSB1'}

## For testing
ports = {'P1': 'COM11',
         'P2': 'COM22'}
## Testing ends

## RFID tag number and some name
rats = {'001': 'Steve',
        '002': 'Julia',
        '003': 'Mario'}

## Open all ports and start reading
for dooraddr in ports.itervalues():
    reader = Serial(dooraddr, baudrate=9600)
    thread = threading.Thread(target=serial_read, args=(reader, queue, dooraddr),).start()

outfile = 'log_rats.dat'
o = open(outfile, 'a', 0)
while True:
    result = get_all_queue_result(queue)
    for aa in result:
        o.write(aa+'\n')
o.close()
