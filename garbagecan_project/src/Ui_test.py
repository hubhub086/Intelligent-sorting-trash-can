# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/caosongliang/VSCodeProject/python/garbagecan_project/src/test.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1190, 606)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.wgt_player = QVideoWidget(self.centralwidget)
        self.wgt_player.setGeometry(QtCore.QRect(10, 120, 421, 281))
        self.wgt_player.setObjectName("wgt_player")
        self.btn_play = QtWidgets.QPushButton(self.centralwidget)
        self.btn_play.setGeometry(QtCore.QRect(10, 460, 101, 41))
        self.btn_play.setObjectName("btn_play")
        self.btn_pause = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pause.setGeometry(QtCore.QRect(170, 460, 101, 41))
        self.btn_pause.setObjectName("btn_pause")
        self.btn_select = QtWidgets.QPushButton(self.centralwidget)
        self.btn_select.setGeometry(QtCore.QRect(330, 460, 101, 41))
        self.btn_select.setObjectName("btn_select")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(130, 90, 131, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 90, 71, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.sld_duration = QtWidgets.QSlider(self.centralwidget)
        self.sld_duration.setGeometry(QtCore.QRect(10, 420, 361, 16))
        self.sld_duration.setOrientation(QtCore.Qt.Horizontal)
        self.sld_duration.setObjectName("sld_duration")
        self.lab_duration = QtWidgets.QLabel(self.centralwidget)
        self.lab_duration.setGeometry(QtCore.QRect(390, 420, 31, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lab_duration.setFont(font)
        self.lab_duration.setObjectName("lab_duration")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 0, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 40, 71, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(470, 120, 256, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.carmeralabel = QtWidgets.QLabel(self.centralwidget)
        self.carmeralabel.setGeometry(QtCore.QRect(740, 120, 420, 280))
        self.carmeralabel.setText("")
        self.carmeralabel.setObjectName("carmeralabel")
        self.showcarmera = QtWidgets.QPushButton(self.centralwidget)
        self.showcarmera.setGeometry(QtCore.QRect(780, 460, 101, 41))
        self.showcarmera.setObjectName("showcarmera")
        self.data_analyze = QtWidgets.QPushButton(self.centralwidget)
        self.data_analyze.setGeometry(QtCore.QRect(1040, 460, 101, 41))
        self.data_analyze.setObjectName("data_analyze")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(530, 410, 131, 41))
        self.radioButton.setObjectName("radioButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1190, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_play.setText(_translate("MainWindow", "播放视频"))
        self.btn_pause.setText(_translate("MainWindow", "停止播放"))
        self.btn_select.setText(_translate("MainWindow", "打开"))
        self.label_1.setText(_translate("MainWindow", "垃圾分类宣传视频"))
        self.label_2.setText(_translate("MainWindow", "垃圾识别"))
        self.lab_duration.setText(_translate("MainWindow", "--/--"))
        self.label.setText(_translate("MainWindow", "智能垃圾分类    "))
        self.label_4.setText(_translate("MainWindow", "——K06"))
        self.showcarmera.setText(_translate("MainWindow", "实时显示"))
        self.data_analyze.setText(_translate("MainWindow", "数据分析"))
        self.radioButton.setText(_translate("MainWindow", "满载提示"))
from PyQt5.QtMultimediaWidgets import QVideoWidget
