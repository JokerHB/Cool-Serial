#include "basecom.h"

Basecom::Basecom()
{
       this->ReSet();
}


Basecom::~Basecom()
{
    if(serialPort.isOpen())
    {
        serialPort.close();
    }
}


QStringList Basecom::GetComInfo()
{
    QStringList comInfo;

    foreach (const QSerialPortInfo &info, QSerialPortInfo::availablePorts())  
    {  
        // qDebug()<<"Name:"<<info.portName();  
        // qDebug()<<"Description:"<<info.description();  
        // qDebug()<<"Manufacturer:"<<info.manufacturer();  
  
        QSerialPort serial;  
        serial.setPort(info);  
        if(serial.open(QIODevice::ReadWrite))  
        {   
            comInfo.append(info.portName());
            serial.close();  
        }  
    }  
    return comInfo;
}

bool Basecom::SetCom(QString com, QString boundRate, QString checkBit, QString dataBits, QString stopBit)
{ 
    serialPort.setPortName(com);  

    if(serialPort.open(QIODevice::ReadWrite))  
    {  
        serialPort.setBaudRate(boundRate.toInt());  
        serialPort.setFlowControl(QSerialPort::NoFlowControl); 
        
        if(dataBits == "8")
        {
             serialPort.setDataBits(QSerialPort::Data8); 
        }
        else
        {
             serialPort.setDataBits(QSerialPort::Data7); 
        }

        if(stopBit == "1") 
        {
            serialPort.setStopBits(QSerialPort::OneStop);  
        }
        else
        {
            serialPort.setStopBits(QSerialPort::TwoStop);  
        }

        if(checkBit == "Odd")
        {
            serialPort.setParity(QSerialPort::OddParity);  
        }
        else if (checkBit == "Even")
        {
            serialPort.setParity(QSerialPort::EvenParity);  
        }
        else
        {
            serialPort.setParity(QSerialPort::NoParity);  
        }
        serialPort.clearError();
        serialPort.clear();

        //QTimer* timer = new QTimer(this);
        //connect(timer, SIGNAL(timeout()), this, SLOT(readyReadSlot()));
        //timer->start(1000);

        connect(&serialPort, SIGNAL(readyRead()), this, SLOT(readyReadSlot()));

        return true;
    }  
    else  
    {  
        QMessageBox::about(NULL, "提示", "串口没有打开！");  
        return false;  
    }  
}  

bool Basecom::IsConnect()
{
    return serialPort.isOpen();
}

void Basecom::SwitchOff()
{
    if(this->IsConnect())
    {
        serialPort.close();
    }
}

int Basecom::SendData(QString filepath, QString destname)
{
    this->filename = filepath;
    this->destname = destname;

    return 1;
}

QByteArray Basecom::ReaderBuffer()
{
    QByteArray readComData = serialPort.readAll();

    if(readComData != NULL)
        return readComData;
}

int Basecom::WriteBuffer(QByteArray data)
{
    serialPort.write(data);
    return 1;
}

int Basecom::readyReadSlot()
{
    QByteArray data = this->ReaderBuffer();
    // static bool flag = true;
    // static bool lock = true;


    Sleep(800);

    if(this->lock)
    {
        this->lock = false;

        if(data != NULL)
        {
            int intData = data.toInt();
            // qDebug()<<intData<<endl;
            if(intData >= 0 && intData <= 255 && flag)
            {
                qDebug() << "hhhhh"<<endl;
                // this->WriteBuffer(QByteArray().setNum(intData + 1));
                this->SendToDevice();
                this->flag = false;
                this->lock = true;
                return 0;
            }
            if(this->flag == false)
            {
                qDebug() <<"file size is " << this->filesize<<endl;
                qDebug() <<"rev size is " << intData<<endl;
                if (this->filesize - intData <= 100)
                {
                     serialPort.write("2333");
                     emit FinishTransfer();
                     this->lock = false;
                     return 0;
                }
            }
        }
        this->lock = true;
    }
    return 0;
}

int Basecom::SendToDevice()
{
    serialPort.clear();

    QFile file(this->filename);

    if(!file.open(QIODevice::ReadOnly))
    {
        QMessageBox::warning(NULL,"错误", "不能打开端口", QMessageBox::Yes);
        return -1;
    }

    QByteArray content = destname.toLatin1();
    content.append(' ');
    content.append(file.readAll());
    this->filesize = content.length();
    this->WriteBuffer(content);
    // Sleep(5000);
    this->WriteBuffer("233333");
}

void Basecom::ReSet()
{
    this->flag = true;
    this->lock = true;
}
