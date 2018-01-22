# -*- coding: UTF-8 -*-

import os
import sys
import time
import serial

ser = serial.Serial(timeout=0, port='/dev/ttyUSB0', baudrate=int(sys.argv[1]), parity=serial.PARITY_ODD, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, rtscts = True)

dataSize = ser.inWaiting()
currentTime = time.time()
data = ''
while dataSize > 0:
    data += ser.read(dataSize)
    dataSize = ser.inWaiting()

print 'len %d' % len(data)
print 'time %f' % (time.time() - currentTime)
    