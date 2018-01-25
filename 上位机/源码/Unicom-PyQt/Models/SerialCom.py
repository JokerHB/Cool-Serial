# -*- coding: UTF-8 -*-

import serial

class SerialCom(object):
    def __init__(self, portName, boundRate=9600, dataBits=8, stopBits=1, checkType='Odd'):
        super(SerialCom, self).__init__()
        self.__portName__ = portName
        self.__boundRate__ = boundRate
        self.__dataBits__ = dataBits
        self.__stopBits__ = stopBits
        if checkType == 'Odd':
            self.__chechType__ = serial.PARITY_ODD
        elif checkType == 'Even':
            self.__chechType__ = serial.PARITY_EVEN
        else:
            self.__chechType__ = serial.PARITY_NONE

    def OpenSerCom(self):
        if self.__portName__ == None:
            print 'Error#1 can not open without port name'
            return None
        try:
            self.__ser__ = serial.Serial(port=self.__portName__, baudrate=self.__boundRate__, parity=self.__chechType__,
                                         stopbits=self.__stopBits__, bytesize=self.__dataBits__, rtscts=True)
            self.__ser__.flushInput()
            self.__ser__.flushOutput()
            self.__ser__.flush()
        except Exception, e:
            print 'Error#2 can not open serial port %s' % str(e)
            return None
        return True

    def CloseSerCom(self):
        if self.IsOpen():
            self.__ser__.close()

    def FlushIO(self):
        if self.IsOpen():
            self.__ser__.flushInput()
            self.__ser__.flushOutput()
            self.__ser__.flush()

    def IsOpen(self):
        if self.__ser__ == None:
            return False
        return True

    def WriteData(self, data):
        if self.IsOpen() == False:
            print 'Error#3 please open serial port before transfer'
            return None
        self.__ser__.write(data)
        return True

    def InWaiting(self):
        if self.IsOpen():
            return self.__ser__.inWaiting()
        return None

    def ReadData(self, length=1):
        if self.IsOpen():
            return self.__ser__.read(size=length)
        return None

    def ReadAll(self):
        if self.IsOpen():
            return self.__ser__.read(size=self.__ser__.inWaiting())
        return None

    @staticmethod
    def SerialComList():
        import serial.tools.list_ports
        serList = list(serial.tools.list_ports.comports())
        comList = []
        if len(serList) <= 0:
            print 'Warning#1 there is no serial com'
            return comList
        for ser in serList:
            comList.append(ser[0])
        return comList
