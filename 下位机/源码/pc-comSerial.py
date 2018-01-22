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
        ser = serial.Serial(port='COM3', baudrate=921600, parity=serial.PARITY_ODD, stopbits=serial.STOPBITS_TWO, bytesize=serial.EIGHTBITS, rtscts = True)
    except Exception, e:
        print e
        return
    
    ser.flushInput()
    ser.flushOutput()

    serData = ser.read()
    serDataLen = ser.inWaiting()
    
    if serDataLen > 0:
        serData += ser.read(serDataLen)
        ser.write(str(int(serData) + 1))
        time.sleep(2)
        ser.write(fileName + ' ' + data)
        time.sleep(1)
        ser.write('233333')
        time.sleep(1)
        serDataLen = ser.inWaiting()
        data = ser.read(serDataLen)
        ser.write(data)

if __name__ == '__main__':
    main()
