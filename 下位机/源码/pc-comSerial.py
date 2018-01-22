# -*- coding: UTF-8 -*-

import os
import sys
import time
import serial

def main():
    fileName = './transfile.txt'
    f = open(fileName, 'rb')
    data = f.read()
    f.close()
    
    try:
        ser = serial.Serial(port='COM4', baudrate=115200, parity=serial.PARITY_ODD, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, rtscts = True)
    except Exception, e:
        print e
        return
    
    ser.flushInput()
    ser.flushOutput()

    serData = ser.read()
    serDataLen = ser.inWaiting()
    
    if serDataLen > 0:
        serData += ser.read(serDataLen)
        print serData
        ser.write(str(int(serData) + 1))
        time.sleep(2)
        ser.write(fileName + ' ' + data)
    ser.write('233333')



if __name__ == '__main__':
    main()
