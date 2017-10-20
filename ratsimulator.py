#!/usr/bin/env python
#-*- coding: utf-8 -*-

import numpy as np
import time
import os

## Serial port simulation ##
from Rat import Rat

ports = {'P1': 'COM11',
         'P2': 'COM22'}

# Register rats; ids should match whatever ID comes out of the RFID reader
rat1 = Rat('Steve', '001')
rat2 = Rat('Julia', '002')
rat3 = Rat('Mario', '003')

rats = [rat1, rat2, rat3]

for a in range(10):
    rid = np.random.randint(len(rats))
    pid = np.random.randint(len(ports))
    cmd = 'echo %s > %s' % (rats[rid].rfid, ports[ports.keys()[pid]])
    print cmd
    os.system(cmd)
    time.sleep(2*np.random.rand())
