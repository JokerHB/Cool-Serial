#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "basecom.h"
#include <QFileDialog>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    com = new Basecom();

    // set boxes font
    ui->cmb_serialPort->setFont(ui->label_serialPort->font());
    ui->cmb_boundRate->setFont(ui->label_serialPort->font());
    ui->cmb_checkBit->setFont(ui->label_serialPort->font());
    ui->cmb_dataBits->setFont(ui->label_serialPort->font());
    ui->cmb_stopBit->setFont(ui->label_serialPort->font());
    ui->label_filePath->setFont(ui->label_serialPort->font());
    ui->btn_selectFile->setFont(ui->label_serialPort->font());
    ui->btn_connect->setFont(ui->label_serialPort->font());
    ui->pb_sendProgress->setFont(ui->label_serialPort->font());

    // set button text
    ui->btn_connect->setText("连接");
    ui->btn_selectFile->setText("选择文件");
    ui->label_filePath->setText("请选择文件");

    // set layout
    ui->label_serialPort->setGeometry(20, 30, 60, 30);
    ui->cmb_serialPort->setGeometry(ui->label_serialPort->x() + ui->label_serialPort->width() + 5, ui->label_serialPort->y(), 100, 30);
    ui->label_boundRate->setGeometry(ui->cmb_serialPort->x() + ui->cmb_serialPort->width() + 20, ui->label_serialPort->y(), 60, 30);
    ui->cmb_boundRate->setGeometry(ui->label_boundRate->x() + ui->label_boundRate->width() + 5, ui->label_serialPort->y(), 100, 30);
    ui->label_dataBits->setGeometry(ui->cmb_boundRate->x() + ui->cmb_boundRate->width() + 20, ui->label_serialPort->y(), 60, 30);
    ui->cmb_dataBits->setGeometry(ui->label_dataBits->x() + ui->label_dataBits->width() + 5, ui->label_serialPort->y(), 100, 30);
    ui->label_chechBit->setGeometry(ui->label_serialPort->x(), ui->label_serialPort->y() + 50, 60, 30);
    ui->cmb_checkBit->setGeometry(ui->cmb_serialPort->x(), ui->label_chechBit->y(), 100, 30);
    ui->label_stopBit->setGeometry(ui->label_boundRate->x(), ui->label_chechBit->y(), 60, 30);
    ui->cmb_stopBit->setGeometry(ui->cmb_boundRate->x(), ui->label_chechBit->y(), 100, 30);
    ui->btn_connect->setGeometry(ui->label_dataBits->x() + 45, ui->label_chechBit->y(), 100, 30);
    ui->btn_selectFile->setGeometry(ui->btn_connect->x(), ui->btn_connect->y() + 50, 100, 30);
    ui->label_filePath->setGeometry(ui->label_chechBit->x(), ui->btn_selectFile->y(), 400, 30);
    ui->pb_sendProgress->setGeometry(ui->label_filePath->x(), ui->label_filePath->y() + 50, 500, 30);

    // add info
    ui->cmb_serialPort->addItems(com->GetComInfo());
    ui->cmb_boundRate->addItems(qsl_boundRate);
    ui->cmb_checkBit->addItems(qsl_checkBit);
    ui->cmb_dataBits->addItems(qsl_dataBits);
    ui->cmb_stopBit->addItems(qsl_stopBit);

    ui->cmb_boundRate->setCurrentIndex(2);
    ui->cmb_dataBits->setCurrentIndex(1);

    ui->label_filePath->setWordWrap(true);
    ui->btn_selectFile->setDisabled(true);
    ui->pb_sendProgress->setHidden(true);
    ui->pb_sendProgress->setValue(0.0);

    connect(com, SIGNAL(FinishTransfer()), this, SLOT(ResetTranser()));
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_btn_selectFile_clicked()
{
    QString filename;
    filename = QFileDialog::getOpenFileName(this, tr("选择文件"), "", tr("Files (*.*)"));

    if(filename.isEmpty())
    {
        return ;
    }
    else
    {
        QStringList shortName = filename.split('/');
        ui->label_filePath->setText(shortName[shortName.length() - 1]);
    }

    ui->btn_selectFile->setDisabled(true);

    com->SendData(filename, filename.split('/')[filename.split('/').length() - 1]);
}

void MainWindow::on_btn_connect_clicked()
{
    if(com != NULL && com->IsConnect())
    {
        ui->btn_connect->setText("连接");
        ui->btn_selectFile->setDisabled(true);
        com->SwitchOff();
    }
    else
    {
        if(com->SetCom(ui->cmb_serialPort->currentText(), ui->cmb_boundRate->currentText(), ui->cmb_checkBit->currentText(), ui->cmb_dataBits->currentText(), ui->cmb_stopBit->currentText()))
        {
            ui->btn_connect->setText("断开");
            ui->btn_selectFile->setDisabled(false);
        }
    }

}

void MainWindow:: ResetTranser()
{
    ui->btn_selectFile->setDisabled(false);
    QMessageBox::about(NULL, tr("完成"), "完成");
    // this->on_btn_connect_clicked();
    com->ReSet();
}
