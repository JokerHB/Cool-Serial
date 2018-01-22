#ifndef BASECOM_H
#define BASECOM_H

#include <iostream>
#include <string>
#include <QSerialPort>  
#include <QSerialPortInfo>  
#include <QMessageBox>
#include <QFile>
#include <QDebug>
#include <windows.h>
#include <QTime>
#include <QTimer>

using namespace std;

const static QStringList qsl_boundRate = {"2400", "4800", "9600", "115200"};
const static QStringList qsl_dataBits = {"7", "8"};
const static QStringList qsl_checkBit = {"Odd", "Even", "None"};
const static QStringList qsl_stopBit = {"1", "2"};

class Basecom : public QObject
{
    Q_OBJECT

public:
    Basecom();

    ~Basecom();

    QStringList GetComInfo();

    bool IsConnect();

    void SwitchOff();

    bool SetCom(QString com, QString boundRate, QString checkBit, QString dataBits, QString stopBit);

    int SendData(QString filepath, QString destname);

    QByteArray ReaderBuffer();

    int WriteBuffer(QByteArray data);

    int SendToDevice();

    void ReSet();

signals:
    void FinishTransfer();

public slots:
    int readyReadSlot();

private:
    QSerialPort serialPort;

    QString destname;

    QString filename;

    qint64 filesize;

    bool flag;

    bool lock;

};

struct Content{
  int len;
  char data[];
};

#endif // BASECOM_H
