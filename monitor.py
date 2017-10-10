#!/usr/bin/env python
#-*- coding: utf-8 -*-

import numpy as np
import serial
import Queue
import threading

## Serial port simulation ##
import os, pty, serial
from Rat import Rat

## Define some Serial read functions
queue = Queue.Queue(0)

def serial_read(s):
    while True:
        line = s.readline()
        queue.put(line)

# Define topology and port properties
# -----------------------------------------------
# |        |        |         |        |        |
# |        P1       P2        P3       P4       |
# |        |        |         |        |        |
# -----------------------------------------------

ports = {'P1': '/dev/ttyUSB0',
         'P2': '/dev/ttyUSB1',
         'P3': '/dev/ttyUSB2',
         'P4': '/dev/ttyUSB3'}

ports = {'P1': '/dev/pts/20'}

# Register rats; ids should match whatever ID comes out of the RFID reader
rat1 = Rat('Steve', '001')
rat2 = Rat('Julia', '002')
rat3 = Rat('Mario', '003')

for dooraddr in ports.itervalues():
    reader = serial.Serial(dooraddr, baudrate=9600)
    thread = threading.Thread(target=serial_read, args=(reader,),).start()

for a in queue:
    print a
