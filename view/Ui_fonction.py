#!/usr/bin/python3
#coding:utf-8
from bloogui import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


from Ui_fonction import *



class Mainwindow(QMainWindow):
	"""docstring for Mainwindow"""
	
	def __init__(self):
		QMainWindow.__init__(self)
		self.showMaximized()
		self.ui= Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.btn_toggle.clicked.connect(lambda: Ui_function.toggleMenu(self,650,True))
		#self.ui.frame_top_menu.setFrame()
		## SHOW MAIN WINDOW
	
		self.show()


class Ui_function(Mainwindow):
	"""docstring for Ui_function"""
	
	def toggleMenu(self,maxWidth ,enable):
			


			if enable:

				#get width 
				width = self.ui.frame_left_menu.width()
				maxExtend = maxWidth
				standard = 1 
				#set Mac Width 
				if width == 1:
					widthExtended = maxExtend
				else :
					widthExtended = standard
				
				#ANIMATION
				self.animation = QPropertyAnimation(self.ui.frame_left_menu,b"minimumWidth")
				self.animation.setDuration(400)
				self.animation.setStartValue(width)
				self.animation.setEndValue(widthExtended)
				self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
				self.animation.start()


			pass	