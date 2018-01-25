# -*- coding: UTF-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from Models.SerialCom import SerialCom

class Test(QWidget):
    def __init__(self):
        super(Test, self).__init__()

        self._grid = QGridLayout()
        self.setLayout(self._grid)

        self._btn = QPushButton('test')
        self._btn.clicked.connect(self.TestFunction)

        self._grid.addWidget(self._btn, 1, 1)

        self.resize(500, 500)

        print SerialCom.SerialComList()

    def TestFunction(self):
        print self.sender().text()
        pass

class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()

        # get labels
        self.label_serCom = QLabel('串口')
        self.label_boundRate = QLabel('波特率')
        self.label_dataBits = QLabel('数据位')
        self.label_checkType = QLabel('校验方式')
        self.label_stopBits = QLabel('停止位')
        self.label_filePath = QLabel('文件路径')

        # get cmbs
        self.cmb_serCom = QComboBox()
        self.cmb_boundRate = QComboBox()
        self.cmb_dataBits = QComboBox()
        self.cmb_checkType = QComboBox()
        self.cmb_stopBits = QComboBox()

        # get buttons
        self.btn_connect = QPushButton('连接')
        self.btn_select = QPushButton('选择')

        # set buttons action
        self.btn_connect.clicked.connect(self.ConnectToSerCom)
        self.btn_select.clicked.connect(self.SendFile)
        self.btn_select.setDisabled(True)

        # set cmb content
        self.cmb_serCom.addItems(SerialCom.SerialComList())
        self.cmb_boundRate.addItems(['50', '75', '110', '134', '150', '200', '300', '600', '1200', '1800', '2400', '4800', '9600', '19200', '38400', '57600', '115200', '230400', '460800', '500000', '576000', '921600', '1000000', '1152000', '1500000', '2000000', '2500000', '3000000', '3500000', '4000000'])
        self.cmb_dataBits.addItems(['6', '7', '8'])
        self.cmb_checkType.addItems(['Odd', 'Even', 'None'])
        self.cmb_stopBits.addItems(['1', '2'])

        # set std font
        self.__stdFont__ = QFont('宋体', 20)
        self.label_serCom.setFont(self.__stdFont__)
        self.label_boundRate.setFont(self.__stdFont__)
        self.label_dataBits.setFont(self.__stdFont__)
        self.label_checkType.setFont(self.__stdFont__)
        self.label_stopBits.setFont(self.__stdFont__)
        self.label_filePath.setFont(self.__stdFont__)
        self.cmb_serCom.setFont(self.__stdFont__)
        self.cmb_boundRate.setFont(self.__stdFont__)
        self.cmb_dataBits.setFont(self.__stdFont__)
        self.cmb_checkType.setFont(self.__stdFont__)
        self.cmb_stopBits.setFont(self.__stdFont__)
        self.btn_connect.setFont(self.__stdFont__)
        self.btn_select.setFont(self.__stdFont__)

        # set std size
        self.__baseL__ = 100
        # self.__width__ = self.__baseL__ * 3. + 50.
        # self.__height__ = self.__baseL__ * (45. / 16.) + 60.
        self.__width__ = 600
        self.__height__ = 300
        self.__stdSize = QSize(self.__baseL__, (9. / 16.) * self.__baseL__)

        # set widgets size
        self.label_serCom.resize(self.__stdSize)
        self.label_boundRate.resize(self.__stdSize)
        self.label_dataBits.resize(self.__stdSize)
        self.label_checkType.resize(self.__stdSize)
        self.label_stopBits.resize(self.__stdSize)
        self.label_filePath.resize(2 * self.__baseL__, (9. / 16.) * self.__baseL__)
        self.cmb_serCom.resize(self.__stdSize)
        self.cmb_boundRate.resize(self.__stdSize)
        self.cmb_dataBits.resize(self.__stdSize)
        self.cmb_checkType.resize(self.__stdSize)
        self.cmb_stopBits.resize(self.__stdSize)
        self.btn_connect.resize(self.__stdSize)
        self.btn_select.resize(self.__stdSize)

        # get layout
        self.globalGrid = QGridLayout()
        self.hbox_line1 = QHBoxLayout()
        self.hbox_line2 = QHBoxLayout()
        self.hbox_line3 = QHBoxLayout()
        self.vhox_ver1 = QVBoxLayout()
        self.vhox_ver2 = QVBoxLayout()
        self.vhox_ver3 = QVBoxLayout()
        self.vhox_ver4 = QVBoxLayout()
        self.vhox_ver5 = QVBoxLayout()

        # set layout
        self.globalGrid.setSpacing(10)
        self.hbox_line1.setSpacing(10)
        self.hbox_line2.setSpacing(10)
        self.hbox_line3.setSpacing(10)
        self.vhox_ver1.setSpacing(5)
        self.vhox_ver2.setSpacing(5)
        self.vhox_ver3.setSpacing(5)
        self.vhox_ver4.setSpacing(5)
        self.vhox_ver5.setSpacing(5)
        # self.hbox_line1.addStretch(1)
        # self.hbox_line2.addStretch(1)
        # self.hbox_line3.addStretch(1)
        self.vhox_ver1.addStretch(1)
        self.vhox_ver2.addStretch(1)
        self.vhox_ver3.addStretch(1)
        self.vhox_ver4.addStretch(1)
        self.vhox_ver5.addStretch(1)

        # add widgets to ver-box
        self.vhox_ver1.addWidget(self.label_serCom)
        self.vhox_ver1.addWidget(self.cmb_serCom)
        self.vhox_ver2.addWidget(self.label_boundRate)
        self.vhox_ver2.addWidget(self.cmb_boundRate)
        self.vhox_ver3.addWidget(self.label_checkType)
        self.vhox_ver3.addWidget(self.cmb_checkType)
        self.vhox_ver4.addWidget(self.label_dataBits)
        self.vhox_ver4.addWidget(self.cmb_dataBits)
        self.vhox_ver5.addWidget(self.label_stopBits)
        self.vhox_ver5.addWidget(self.cmb_stopBits)

        # add ver-layout to her-layout
        self.hbox_line1.addLayout(self.vhox_ver1)
        self.hbox_line1.addLayout(self.vhox_ver2)
        self.hbox_line1.addLayout(self.vhox_ver3)
        self.hbox_line2.addLayout(self.vhox_ver4)
        self.hbox_line2.addLayout(self.vhox_ver5)
        self.hbox_line2.addWidget(self.btn_connect)
        self.hbox_line3.addWidget(self.label_filePath)
        self.hbox_line3.addWidget(self.btn_select)

        # set global layout
        self.globalGrid.addLayout(self.hbox_line1, 0, 0)
        self.globalGrid.addLayout(self.hbox_line2, 1, 0)
        self.globalGrid.addLayout(self.hbox_line3, 2, 0)

        # apply global layout
        self.setLayout(self.globalGrid)
        self.setFixedSize(self.__width__, self.__height__)

        self.__ser__ = None

    def ConnectToSerCom(self):
        serCom = self.cmb_serCom.currentText()
        boundRate = int(self.cmb_boundRate.currentText())
        dataBits = int(self.cmb_dataBits.currentText())
        checkType = self.cmb_checkType.currentText()
        stopBits = int(self.cmb_stopBits.currentText())

        if self.__ser__ != None:
            self.btn_connect.setText('连接')
            self.__ser__.CloseSerCom()
            self.__ser__ = None
            self.btn_select.setDisabled(True)
        else:
            self.__ser__ = SerialCom(portName=serCom, boundRate=boundRate, dataBits=dataBits, stopBits=stopBits, checkType=checkType)
            self.__ser__.OpenSerCom()
            if self.__ser__.IsOpen() != True:
                QMessageBox.question(self, 'Info', 'Can not open com', QMessageBox.Yes)
                self.__ser__ = None
            else:
                self.btn_connect.setText('断开')
                self.btn_select.setDisabled(False)

    def SendFile(self):
        filename = QFileDialog.getOpenFileName(self, '选择文件', '', 'Files (*.*)')[0]
        filename = filename.encode('utf-8')
        if len(filename) <= 0:
            QMessageBox.question(self, 'Info', 'Please select a file', QMessageBox.Yes)
        else:
            shortname = filename.split('/')
            shortname = shortname[len(shortname) - 1]
            self.label_filePath.setText(shortname)
            self.label_filePath.update()
            checkEOF = '7e72284ae5603ef27035446b5946c36c'
            f = open(filename, 'rb')
            data = f.read()
            filelen = len(data)
            f.close()
            self.__ser__.FlushIO()

            serData = self.__ser__.ReadData()
            serDataLen = self.__ser__.InWaiting()

            if serDataLen > 0:
                from time import sleep
                serData += self.__ser__.ReadData(serDataLen)
                print serData
                self.__ser__.WriteData(str(int(serData) + 1))
                sleep(2)
                self.__ser__.WriteData(shortname + ' ' + data + checkEOF)
                sleep(1)
                # self.__ser__.WriteData('233333')
                sleep(1)
                serDataLen = self.__ser__.InWaiting()
                data = self.__ser__.ReadData(serDataLen)
                print data
                self.__ser__.WriteData(data)
                if int(data) == filelen:
                    QMessageBox.question(self, 'Info', 'Success', QMessageBox.Yes)
                self.__ser__.FlushIO()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    # w = Test()
    # center = QDesktopWidget().availableGeometry().center()
    #
    # w.frameGeometry().moveCenter(center)
    #
    # # w.move(w.frameGeometry().topLeft())
    #
    # w.setWindowTitle('Simple')
    #
    # w.show()

    w = Main()

    # set to the center
    center = QDesktopWidget().availableGeometry().center()
    w.frameGeometry().moveCenter(center)

    # show window
    w.show()

    sys.exit(app.exec_())