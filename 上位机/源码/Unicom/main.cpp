#include "mainwindow.h"
#include "basecom.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;

    w.setFixedSize(MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT);
    w.setWindowTitle("Unicom");

    w.show();

    return a.exec();
}
