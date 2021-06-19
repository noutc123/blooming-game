# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game_board.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1208, 864)
        Form.setMinimumSize(QtCore.QSize(1000, 500))
        Form.setStyleSheet("background-color: rgb(45, 45, 45);\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(Form)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top_bar.setStyleSheet("background-color: rgb(35,35 ,35 );")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_top = QtWidgets.QFrame(self.top_bar)
        self.frame_top.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_top.setStyleSheet("background-color: rgb(13, 222, 242);")
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout.addWidget(self.frame_top)
        self.frame_toggle = QtWidgets.QFrame(self.top_bar)
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(Form)
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.verticalLayout.addWidget(self.content)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


class Mainwindow(QMainWindow):
        """docstring for Mainwindow"""

        def __init__(self):
                QMainWindow.__init__(self)
                self.ui =Ui_Form()
                self.ui.setupUi(self)
                self.ui.btn_toggle.clicked.connect(lambda: Ui_function.toggleMenu(self, 650, True))
                self.ui.frame_top_menu.setFrame()
                ## SHOW MAIN WINDOW
                self.show()


class Ui_function(Mainwindow):
        """docstring for Ui_function"""

        def __init__(self):
                self.showFullScreen()
                pass

        def toggleMenu(self, maxWidth, enable):
                fs = self._joueur.get_FinancialStatement

                """self.ui.cash.setObjectName("cash")
                self.ui.cash_value = QtWidgets.QLabel(self.widget)
                self.ui.cash_value.setGeometry(QtCore.QRect(100, 230, 81, 21))
                self.ui.cash_value.setObjectName("cash_value")
                self.ui.T_income = QtWidgets.QLabel(self.widget)
                self.ui.T_income.setGeometry(QtCore.QRect(10, 270, 71, 31))
                self.ui.T_income.setStyleSheet("font: 25 italic 9pt \"Ubuntu\";")
                self.ui.T_income.setObjectName("T_income")
                self.ui.t_Expense = QtWidgets.QLabel(self.widget)
                self.ui.t_Expense.setGeometry(QtCore.QRect(10, 300, 71, 31))
                self.ui.t_Expense.setStyleSheet("font: 25 italic 9pt \"Ubuntu\";")
                self.ui.t_Expense.setObjectName("t_Expense")
                self.ui.cash_value_2 = QtWidgets.QLabel(self.widget)
                self.ui.cash_value_2.setGeometry(QtCore.QRect(120, 270, 61, 21))
                self.ui.cash_value_2.setObjectName("cash_value_2")
                self.ui.cash_value_3 = QtWidgets.QLabel(self.widget)
                self.ui.cash_value_3.setGeometry(QtCore.QRect(120, 300, 61, 21))
                self.ui.cash_value_3.setObjectName("cash_value_3")"""
                self.ui.cash_value.setText("1300 $")
                self.ui.cash_value_2.setText("1300 $")
                self.ui.cash_value_3.setText("1300 $")
                if enable:

                        # get width
                        width = self.ui.frame_left_menu.width()
                        maxExtend = maxWidth
                        standard = 1
                        # set Mac Width
                        if width == 1:
                                widthExtended = maxExtend
                        else:
                                widthExtended = standard

                        # ANIMATION
                        self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
                        self.animation.setDuration(400)
                        self.animation.setStartValue(width)
                        self.animation.setEndValue(widthExtended)
                        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                        self.animation.start()

                pass
if __name__ = "__main__":
        Ui_function()