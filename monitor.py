#!/usr/bin/env python
#-*- coding: utf-8 -*-

import numpy as np
import serial
import Queue
import threading

## Serial port simulation ##
import os, pty, serial




## END ##


from Rat import Rat

## Define some Serial read functions
queue = Queue.Queue(1000)

def serial_read(s):
    while True:
        line = s.readline()
        queue.put(line)

serial0 = serial.Serial('/dev/ttyUSB0')
serial1 = serial.Serial('/dev/ttyUSB1')

thread1 = threading.Thread(target=serial_read, args=(serial0,),).start()
thread2 = threading.Thread(target=serial_read, args=(serial1,),).start()


#register rats
rat1 = Rat('Steve', '001')
rat2 = Rat('Julia', '002')
rat3 = Rat('Mario', '003')
