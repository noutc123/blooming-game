# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Choose_dream.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from model.Player import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dream_label(object):
    def setupUi(self, dream_label):
        dream_label.setObjectName("dream_label")
        dream_label.resize(348, 550)
        dream_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        dream_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(dream_label)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(dream_label)
        self.stackedWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.487562, y1:0.045, x2:0.493, y2:0.045, stop:0 rgba(117, 80, 123, 196), stop:1 rgba(117, 80, 123, 174));")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.page_3)
        self.stackedWidget_2.setGeometry(QtCore.QRect(0, 0, 371, 461))
        self.stackedWidget_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.487562, y1:0.045, x2:0.493, y2:0.045, stop:0 rgba(222, 184, 135, 229), stop:1 rgba(222, 184, 135, 232));")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.stackedWidget_2.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.frame_2 = QtWidgets.QFrame(self.page_7)
        self.frame_2.setGeometry(QtCore.QRect(0, 88, 301, 231))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.dream_Description = QtWidgets.QLabel(self.frame_2)
        self.dream_Description.setGeometry(QtCore.QRect(10, 40, 351, 51))
        self.dream_Description.setStyleSheet("background-color: rgb(222, 184, 135);")
        self.dream_Description.setText("")
        self.dream_Description.setObjectName("dream_Description")
        self.Profession_info = QtWidgets.QLabel(self.frame_2)
        self.Profession_info.setGeometry(QtCore.QRect(6, 116, 361, 111))
        self.Profession_info.setText("")
        self.Profession_info.setObjectName("Profession_info")
        self.label_17 = QtWidgets.QLabel(self.frame_2)
        self.label_17.setGeometry(QtCore.QRect(20, 0, 261, 20))
        self.label_17.setStyleSheet("font: 57 bold 13pt \"Ubuntu\";\n"
"color: rgb(117, 80, 123);")
        self.label_17.setObjectName("label_17")
        self.btn_next = QtWidgets.QPushButton(self.page_7)
        self.btn_next.setGeometry(QtCore.QRect(290, 20, 20, 20))
        self.btn_next.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_next.setStyleSheet("border:0px solid\n"
"")
        self.btn_next.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/side menu tutorial/icons/chevrons-right.svg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.btn_next.setIcon(icon)
        self.btn_next.setIconSize(QtCore.QSize(20, 20))
        self.btn_next.setAutoRepeat(False)
        self.btn_next.setObjectName("btn_next")
        self.btn_prev = QtWidgets.QPushButton(self.page_7)
        self.btn_prev.setGeometry(QtCore.QRect(40, 20, 20, 20))
        self.btn_prev.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_prev.setStyleSheet("border:0px solid\n"
"")
        self.btn_prev.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Downloads/side menu tutorial/icons/chevrons-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("../../../Downloads/side menu tutorial/icons/chevrons-left.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("../../../Downloads/side menu tutorial/icons/chevrons-left.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.btn_prev.setIcon(icon1)
        self.btn_prev.setIconSize(QtCore.QSize(20, 20))
        self.btn_prev.setObjectName("btn_prev")
        self.image_Dream = QtWidgets.QLabel(self.page_7)
        self.image_Dream.setGeometry(QtCore.QRect(86, 20, 181, 61))
        self.image_Dream.setStyleSheet("border-image: url(:/icons/icons/upload-cloud.svg);")
        self.image_Dream.setText("")
        self.image_Dream.setObjectName("image_Dream")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 420, 89, 25))
        self.pushButton_2.setStyleSheet("background-color: rgb(222, 184, 135);\n"
"color: rgb(117, 80, 123);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget_2.addWidget(self.page_7)
        self.stackedWidget.addWidget(self.page_3)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(dream_label)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)
        self.btn_next.clicked.connect(self.next_Dream)
        self.btn_prev.clicked.connect(self.next_Dream)
        self.pushButton_2.clicked.connect(self.Profession_info.clear)
        QtCore.QMetaObject.connectSlotsByName(dream_label)
    def next_Dream(self):
        play = Player("noutch")

        #text = "Your Profession is :"+l[0]+ "your Starting salary is:  "+l[1]+" "


        # self.Profession_info.setText("dream_labeltext")
    def retranslateUi(self, dream_label):
        _translate = QtCore.QCoreApplication.translate
        dream_label.setWindowTitle(_translate("dream_label", "Frame"))
        self.label_17.setText(_translate("dream_label", "Player  choose your DREAM"))
        self.pushButton_2.setText(_translate("dream_label", "CHOOSE"))
        self.Profession_info.setText(_translate("dream_label", "manger ave barack obama a londre"))
        self.btn_next.clicked.connect(self.next_Dream)
        self.btn_prev.clicked.connect(self.next_Dream)
import icons

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dream_label = QtWidgets.QFrame()
    ui = Ui_dream_label()
    ui.setupUi(dream_label)
    dream_label.show()
    sys.exit(app.exec_())

