import sys
from PyQt4 import QtCore, QtGui, uic
import ui_main
import os,time

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class ExampleApp(QtGui.QMainWindow, ui_main.Ui_MainWindow):

    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.detectCOM)
        self.pushButton_2.clicked.connect(self.detect)
        self.lcdNumber_2.setProperty("intValue", 200)

    def detectCOM(self):
        print("COM port detecting function called")
    def detect(self):
        print("Graph plotting function called")
        self.mission_time(2)
        self.gps_data(1,2,3,4,5)
        self.bmp_data(1,2,3)
        self.voltage_dial(20)
        self.tilt_data(1,2,3)
        self.packet_cnt(50)
        self.sys_time()
        self.set_telemetry("HEllo tel")

    def mission_time(self,i=0):
        self.lcdNumber_2.setProperty("intValue", i)

    def gps_data(self,lat=0,longi=0,time1=0,sats=0,alt=0):
        self.label_25.setText(_translate("MainWindow", str(lat), None))
        self.label_24.setText(_translate("MainWindow", str(longi), None))
        self.label_23.setText(_translate("MainWindow", str(time1), None))
        self.label_22.setText(_translate("MainWindow", str(sats), None))
        self.label_21.setText(_translate("MainWindow", str(alt), None))

    def bmp_data(self,temp=0,pressure=0,alt=0):
        self.label_46.setText(_translate("MainWindow", str(temp), None))
        self.label_45.setText(_translate("MainWindow", str(pressure), None))
        self.label_43.setText(_translate("MainWindow", str(alt), None))

    def voltage_dial(self,i=0):
        self.dial.setValue(i)

    def tilt_data(self,tiltx=0,tilty=0,tiltz=0):
        self.label_50.setText(_translate("MainWindow", str(tiltx), None))
        self.label_49.setText(_translate("MainWindow", str(tilty), None))
        self.label_48.setText(_translate("MainWindow", str(tiltz), None))

    def packet_cnt(self,count=0):
        self.lcdNumber_3.setProperty("intValue",count)

    def sys_time(self):
        this_moment = QtCore.QTime.currentTime()
        self.timeEdit.setTime(this_moment)

    def set_telemetry(self,text=""):
        self.label_55.setText(_translate("MainWindow", text, None))



def main():
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()