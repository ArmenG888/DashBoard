import sys,os,threading,time
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (
    QCoreApplication, QPropertyAnimation, QDate, QDateTime,
    QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QRegExp)

from ui_dashboard import Ui_MainWindow


class main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()


        threading.Thread(target=self.test).start()
        
        
    def test(self):
        gear = 1
        speed = 0
        while True:
            speed += 1
            if speed % 30 == 0:
                gear += 1
            self.ui.gear.setText(str(gear))
            self.ui.speed.setText(str(speed))
            self.ui.rpm.setText(str(round((speed%30/30+0.1)*6400)))
            self.ui.progressBar_2.setValue((speed%30/30+0.1)*100)
            time.sleep(0.1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = main()
    sys.exit(app.exec_())