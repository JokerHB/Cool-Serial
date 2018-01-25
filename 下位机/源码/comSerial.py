# -*- coding: UTF-8 -*-

import os
import sys
import time
import serial

from random import randint
randomNumber = randint(0, 255)

def IOAcept(ser):
    global randomNumber
    
    ser.write(str(randomNumber))
    time.sleep(1)
    dataSize = ser.inWaiting()
    if dataSize > 0:
        print ser.read(dataSize)
        return True
    time.sleep(0.5)
    return False

def GetFileName(ser):
    fileName = ''
    data = ser.read()
    while data != ' ':
        fileName += str(data)
        data = ser.read()
    return fileName

def GetFile(ser, fileName):
    checkEOF = '7e72284ae5603ef27035446b5946c36c'
    f = open(fileName, 'wb')
    fileSize = ser.inWaiting()
    data = ''
    while(fileSize >= 0):
        if fileSize > 0:
            data += ser.read(fileSize)
            if data[len(data) - len(checkEOF):] == checkEOF:
                data = data[:len(data) - len(checkEOF)]
                break
        fileSize = ser.inWaiting()
    f.write(data)
    f.close()
    ser.write(str(len(data)))
    time.sleep(1)
    dataSize = ser.inWaiting()
    if dataSize > 0:
        print ser.read(dataSize)


def main():
    currentTime = time.time()
    try:
        ser = serial.Serial(timeout=0, port='/dev/ttyUSB0', baudrate=int(sys.argv[1]), parity=serial.PARITY_ODD, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, rtscts = True)
    except Exception, e:
        print e
        return
    
    ser.flushInput()
    ser.flushOutput()
    
    if IOAcept(ser):
        print 'begin rev'
        filename = '/home/pi/' + GetFileName(ser)
        GetFile(ser, filename)
        os.system('sudo chmod 777 ' + filename)
    ser.close()
    print time.time() - currentTime

if __name__ == '__main__':
    main()