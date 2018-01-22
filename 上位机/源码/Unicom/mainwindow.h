#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "basecom.h"

const static int MAIN_WINDOW_WIDTH = 600;
const static int MAIN_WINDOW_HEIGHT = 300;

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_btn_selectFile_clicked();

    void on_btn_connect_clicked();


public slots:
    void  ResetTranser();


private:
    Ui::MainWindow *ui;

    Basecom* com;
};

#endif // MAINWINDOW_H
