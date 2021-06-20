# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from test import *
from PyQt5 import QtCore, QtGui, QtWidgets
from game_test import *
import res, sys


class Ui_Form(QMainWindow):
    switch_window = QtCore.pyqtSignal()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(638, 563)

        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.showFullScreen()
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(70, 20, 491, 511))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(-4, -1, 501, 511))
        self.label.setStyleSheet("\n"
                                 "border-image: url(:/image/res/login.png);\n"
                                 "border-radius:20px\n"
                                 "")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 501, 511))
        self.label_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9),stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\n"
            "border-radius:20px\n"
            "")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(200, 250, 67, 17))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 210, 113, 25))
        self.lineEdit.setStyleSheet("background-color: rgba(0, 0, 0,0);\n"
                                    "border:none;\n"
                                    "border-bottom:2px solid rgba(105,118,132,255);\n"
                                    "color:rgba(255,255,255,230);\n"
                                    "padding-bottom:4px;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(190, 70, 121, 51))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 270, 113, 25))
        self.lineEdit_2.setStyleSheet("background-color: rgba(0, 0, 0,0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(105,118,132,255);\n"
                                      "color:rgba(255,255,255,230);\n"
                                      "padding-bottom:4px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(180, 350, 121, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QpushButton#pushButton{\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(108, 180, 124, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));\n"
                                      "color:rgba(255,255,255,210);\n"
                                      "border-radius:5px;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.gotologin)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "name"))
        self.label_4.setText(_translate("Form", "TextLabel"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "party"))
        self.pushButton.setText(_translate("Form", "start"))

    def gotologin(self):
        self.app.quit

        """
        self.exit = QMessageBox()
        self.exit.setText("vous sorter du jeux voulez sauvegarder ")
        self.exit.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        treval = self.exit.exec()"""


def main():
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()