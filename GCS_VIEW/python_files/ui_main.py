# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Mon May 28 17:32:17 2018
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(803, 662)
        MainWindow.setTabShape(QtGui.QTabWidget.Triangular)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 275, 91))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_2.setStyleSheet(_fromUtf8("border: 3px black;\n"
"font: oblique 17pt \"DejaVu Sans\";\n"
"background: solid gray;\n"
"color: white;\n"
""))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(250, 0, 398, 91))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setStyleSheet(_fromUtf8("border: 3px black;\n"
"font: oblique 30pt \"DejaVu Sans\";\n"
"background: black;\n"
"color: white;\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(620, 0, 181, 176))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_3.setStyleSheet(_fromUtf8(" background-color: white;\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:100px;\n"
" border-color: black;\n"
" max-width:170px;\n"
" max-height:170px;\n"
" min-width:170px;\n"
" min-height:170px;\n"
""))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("../images/2426.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.gridLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(470, 420, 326, 156))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 420, 324, 154))
        self.label_4.setStyleSheet(_fromUtf8(" background-color: white;\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:100px;\n"
" border-color: black;\n"
" max-width:320px;\n"
" max-height:150px;\n"
" min-width:320px;\n"
" min-height:150px;\n"
""))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("../images/acc.PNG")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(460, 90, 161, 81))
        self.lcdNumber.setStyleSheet(_fromUtf8(" border-width:0px;\n"
"\n"
""))
        self.lcdNumber.setDigitCount(4)
        self.lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdNumber.setProperty("intValue", 2426)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 100, 141, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 100, 281, 51))
        self.label_5.setStyleSheet(_fromUtf8("font: oblique 12pt \"DejaVu Sans\";\n"
""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(470, 386, 121, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.timeEdit = QtGui.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(590, 386, 131, 31))
        self.timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit.setReadOnly(True)
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.dial = QtGui.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(269, 440, 111, 91))
        self.dial.setMaximum(50)
        self.dial.setInvertedControls(False)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName(_fromUtf8("dial"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 150, 141, 51))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(300, 520, 16, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(270, 480, 16, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(300, 430, 16, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(350, 430, 16, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(370, 470, 16, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(350, 520, 16, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(220, 380, 221, 52))
        self.widget.setStyleSheet(_fromUtf8("border: 5px black;\n"
"\n"
""))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_13 = QtGui.QLabel(self.widget)
        self.label_13.setStyleSheet(_fromUtf8("font: oblique 15pt \"DejaVu Sans\";\n"
"background: black;\n"
"color: white;\n"
""))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label_13)
        self.lcdNumber_2 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(10, 260, 201, 71))
        self.lcdNumber_2.setSmallDecimalPoint(True)
        self.lcdNumber_2.setProperty("value", 21.0)
        self.lcdNumber_2.setProperty("intValue", 21)
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 220, 201, 31))
        self.label_14.setStyleSheet(_fromUtf8("font: oblique 15pt \"DejaVu Sans\";\n"
"background: black;\n"
"color: white;\n"
""))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 210, 221, 131))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 340, 221, 241))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_15 = QtGui.QLabel(self.frame_2)
        self.label_15.setGeometry(QtCore.QRect(5, 10, 211, 31))
        self.label_15.setStyleSheet(_fromUtf8("font: oblique 15pt \"DejaVu Sans\";\n"
"background: black;\n"
"color: white;\n"
""))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.frame_2)
        self.label_16.setGeometry(QtCore.QRect(10, 60, 71, 17))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.frame_2)
        self.label_17.setGeometry(QtCore.QRect(10, 100, 81, 17))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.frame_2)
        self.label_18.setGeometry(QtCore.QRect(10, 140, 66, 17))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.frame_2)
        self.label_19.setGeometry(QtCore.QRect(10, 170, 141, 17))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.frame_2)
        self.label_20.setGeometry(QtCore.QRect(10, 200, 71, 17))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.frame_2)
        self.label_21.setGeometry(QtCore.QRect(90, 200, 111, 17))
        self.label_21.setStyleSheet(_fromUtf8("border: 3px black;\n"
"font: oblique 13pt \"DejaVu Sans\";\n"
"background: solid gray;\n"
"color: white;\n"
""))
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(self.frame_2)
        self.label_22.setGeometry(QtCore.QRect(90, 169, 111, 21))
        self.label_22.setStyleSheet(_fromUtf8("border: 3px black;\n"
"font: oblique 13pt \"DejaVu Sans\";\n"
"background: solid gray;\n"
"color: white;\n"
""))
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(self.frame_2)
        self.label_23.setGeometry(QtCore.QRect(80, 139, 121, 21))
        self.label_23.setStyleSheet(_fromUtf8("border: 3px black;\n"
"font: oblique 11pt \"DejaVu Sans\";\n"
"background: solid gray;\n"
"color: white;\n"
""))
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_24 = QtGui.QLabel(self.frame_2)
        self.label_24.setGeometry(QtCore.QRect(100, 100, 101, 21))
        self.label_24.setStyleSheet(_fromUtf8("border: 3px black;\n"
"font: oblique 11pt \"DejaVu Sans\";\n"
"background: solid gray;\n"
"color: white;"))
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_25 = QtGui.QLabel(self.frame_2)
        self.label_25.setGeometry(QtCore.QRect(90, 60, 111, 21))
        self.label_25.setStyleSheet(_fromUtf8("border: 3px black;\n"
"font: oblique 11pt \"DejaVu Sans\";\n"
"background: solid gray;\n"
"color: white;\n"
""))
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(220, 210, 221, 171))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.label_37 = QtGui.QLabel(self.frame_3)
        self.label_37.setGeometry(QtCore.QRect(5, 10, 211, 31))
        self.label_37.setStyleSheet(_fromUtf8("font: oblique 15pt \"DejaVu Sans\";\n"
"background: black;\n"
"color: white;\n"
""))
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.label_39 = QtGui.QLabel(self.frame_3)
        self.label_39.setGeometry(QtCore.QRect(10, 60, 51, 17))
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.label_40 = QtGui.QLabel(self.frame_3)
        self.label_40.setGeometry(QtCore.QRect(10, 90, 71, 20))
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.label_42 = QtGui.QLabel(self.frame_3)
        self.label_42.setGeometry(QtCore.QRect(10, 130, 71, 17))
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.label_43 = QtGui.QLabel(self.frame_3)
        self.label_43.setGeometry(QtCore.QRect(100, 130, 111, 21))
        self.label_43.setStyleSheet(_fromUtf8("border: 3px black;\n"
"font: oblique 13pt \"DejaVu Sans\";\n"
"background: solid gray;\n"
"color: white;\n"
""))
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.label_45 = QtGui.QLabel(self.frame_3)
        self.label_45.setGeometry(QtCore.QRect(100, 90, 111, 20))
        self.label_45.setStyleSheet(_fromUtf8("border: 3px black;\n"
"font: oblique 11pt \"DejaVu Sans\";\n"
"background: solid gray;\n"
"color: white;\n"
""))
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.label_46 = QtGui.QLabel(self.frame_3)
        self.label_46.setGeometry(QtCore.QRect(100, 50, 111, 21))
        self.label_46.setStyleSheet(_fromUtf8("border: 3px black;\n"
"font: oblique 11pt \"DejaVu Sans\";\n"
"background: solid gray;\n"
"color: white;"))
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.frame_4 = QtGui.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(450, 210, 221, 171))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.label_38 = QtGui.QLabel(self.frame_4)
        self.label_38.setGeometry(QtCore.QRect(5, 10, 211, 31))
        self.label_38.setStyleSheet(_fromUtf8("font: oblique 15pt \"DejaVu Sans\";\n"
"background: black;\n"
"color: white;\n"
""))
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.label_41 = QtGui.QLabel(self.frame_4)
        self.label_41.setGeometry(QtCore.QRect(10, 60, 51, 17))
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.label_44 = QtGui.QLabel(self.frame_4)
        self.label_44.setGeometry(QtCore.QRect(10, 90, 71, 20))
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.label_47 = QtGui.QLabel(self.frame_4)
        self.label_47.setGeometry(QtCore.QRect(10, 130, 71, 17))
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.label_48 = QtGui.QLabel(self.frame_4)
        self.label_48.setGeometry(QtCore.QRect(100, 131, 111, 20))
        self.label_48.setStyleSheet(_fromUtf8("border: 3px black;\n"
"font: oblique 13pt \"DejaVu Sans\";\n"
"background: solid gray;\n"
"color: white;\n"
""))
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.label_49 = QtGui.QLabel(self.frame_4)
        self.label_49.setGeometry(QtCore.QRect(100, 90, 111, 21))
        self.label_49.setStyleSheet(_fromUtf8("border: 3px black;\n"
"font: oblique 11pt \"DejaVu Sans\";\n"
"background: solid gray;\n"
"color: white;\n"
""))
        self.label_49.setAlignment(QtCore.Qt.AlignCenter)
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.label_50 = QtGui.QLabel(self.frame_4)
        self.label_50.setGeometry(QtCore.QRect(100, 50, 111, 21))
        self.label_50.setStyleSheet(_fromUtf8("border: 3px black;\n"
"font: oblique 11pt \"DejaVu Sans\";\n"
"background: solid gray;\n"
"color: white;"))
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.frame_5 = QtGui.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(680, 209, 120, 171))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.label_51 = QtGui.QLabel(self.frame_5)
        self.label_51.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.label_51.setStyleSheet(_fromUtf8("font: oblique 11pt \"DejaVu Sans\";\n"
"background: black;\n"
"color: white;\n"
""))
        self.label_51.setAlignment(QtCore.Qt.AlignCenter)
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.lcdNumber_3 = QtGui.QLCDNumber(self.frame_5)
        self.lcdNumber_3.setGeometry(QtCore.QRect(13, 60, 101, 61))
        self.lcdNumber_3.setDigitCount(3)
        self.lcdNumber_3.setProperty("intValue", 100)
        self.lcdNumber_3.setObjectName(_fromUtf8("lcdNumber_3"))
        self.label_52 = QtGui.QLabel(self.centralwidget)
        self.label_52.setGeometry(QtCore.QRect(460, 180, 111, 21))
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.label_53 = QtGui.QLabel(self.centralwidget)
        self.label_53.setGeometry(QtCore.QRect(580, 176, 151, 31))
        self.label_53.setObjectName(_fromUtf8("label_53"))
        self.label_54 = QtGui.QLabel(self.centralwidget)
        self.label_54.setGeometry(QtCore.QRect(240, 570, 211, 31))
        self.label_54.setStyleSheet(_fromUtf8("font: oblique 15pt \"DejaVu Sans\";\n"
"background: black;\n"
"color: white;\n"
""))
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setObjectName(_fromUtf8("label_54"))
        self.label_55 = QtGui.QLabel(self.centralwidget)
        self.label_55.setGeometry(QtCore.QRect(30, 610, 741, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_55.setFont(font)
        self.label_55.setStyleSheet(_fromUtf8("border: 3px black;\n"
"font: oblique 11pt \"DejaVu Sans\";\n"
"background: solid gray;\n"
"color: white;"))
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName(_fromUtf8("label_55"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_2.setText(_translate("MainWindow", "Team KALPANA-1      ", None))
        self.label.setText(_translate("MainWindow", "     GCS_VIEW", None))
        self.pushButton.setText(_translate("MainWindow", "DETECT COM PORT", None))
        self.label_5.setText(_translate("MainWindow", "COM SELECTED:", None))
        self.label_6.setText(_translate("MainWindow", "SYSTEM TIME:", None))
        self.pushButton_2.setText(_translate("MainWindow", "PLOT GRAPHS", None))
        self.label_7.setText(_translate("MainWindow", "0", None))
        self.label_8.setText(_translate("MainWindow", "1", None))
        self.label_9.setText(_translate("MainWindow", "2", None))
        self.label_10.setText(_translate("MainWindow", "3", None))
        self.label_11.setText(_translate("MainWindow", "4", None))
        self.label_12.setText(_translate("MainWindow", "5", None))
        self.label_13.setText(_translate("MainWindow", "Voltage indicator", None))
        self.label_14.setText(_translate("MainWindow", "Mission Time", None))
        self.label_15.setText(_translate("MainWindow", "GPS DATA", None))
        self.label_16.setText(_translate("MainWindow", "LATITUDE", None))
        self.label_17.setText(_translate("MainWindow", "LONGITUDE", None))
        self.label_18.setText(_translate("MainWindow", "TIME", None))
        self.label_19.setText(_translate("MainWindow", "SATS", None))
        self.label_20.setText(_translate("MainWindow", "ALTITUDE", None))
        self.label_21.setText(_translate("MainWindow", "0", None))
        self.label_22.setText(_translate("MainWindow", "0", None))
        self.label_23.setText(_translate("MainWindow", "0", None))
        self.label_24.setText(_translate("MainWindow", "0", None))
        self.label_25.setText(_translate("MainWindow", "0", None))
        self.label_37.setText(_translate("MainWindow", "BMP180 DATA", None))
        self.label_39.setText(_translate("MainWindow", "TEMP", None))
        self.label_40.setText(_translate("MainWindow", "PRESSURE", None))
        self.label_42.setText(_translate("MainWindow", "ALTITUDE", None))
        self.label_43.setText(_translate("MainWindow", "0", None))
        self.label_45.setText(_translate("MainWindow", "0", None))
        self.label_46.setText(_translate("MainWindow", "0", None))
        self.label_38.setText(_translate("MainWindow", "TILT DATA", None))
        self.label_41.setText(_translate("MainWindow", "TILT X", None))
        self.label_44.setText(_translate("MainWindow", "TILT Y", None))
        self.label_47.setText(_translate("MainWindow", "TILT Z", None))
        self.label_48.setText(_translate("MainWindow", "0", None))
        self.label_49.setText(_translate("MainWindow", "0", None))
        self.label_50.setText(_translate("MainWindow", "0", None))
        self.label_51.setText(_translate("MainWindow", "PKT. COUNT", None))
        self.label_52.setText(_translate("MainWindow", "Software state:", None))
        self.label_53.setText(_translate("MainWindow", "Default", None))
        self.label_54.setText(_translate("MainWindow", "TELEMETRY", None))
        self.label_55.setText(_translate("MainWindow", "0", None))

