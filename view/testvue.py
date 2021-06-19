#!/usr/bin/python3
#coding:utf-8
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app =QApplication(sys.argv)

scene =QGraphicsScene()
rectangleVerrt = QGraphicsRectItem(1.0,1.0,200,150)
rectangleVerrt.setBrush(QBrush(Qt.lightGray))
rectangleVerrt.setPos(3.0,4.0)
scene.addItem(rectangleVerrt)

x = 12;
y = 36;
lastKeyPress = 'RIGHT'
timer = QBasicTimer()
snakeArray = [[x, y], [x-12, y], [x-24, y]]
def paintEvent(self, event):
		qp = QtGui.QPainter()
		qp.begin()
		pt=drawSnake(qp)
		
def drawSnake(qp):
		qp.setPen(Qt.NoPen)
		qp.setBrush(QColor(255, 80, 0, 255))
		for i in snakeArray:
			qp.drawRect(i[0], i[1], 12, 12)


b = 48.
ox = 4. # largeur
# haueur de oiel 
oy =6. 
smiley = QGraphicsEllipseItem(-b/2 ,-b/2,b,b)
smiley.setBrush(QBrush(Qt.yellow))
yeux =  [QGraphicsEllipseItem(-ox/2.,oy/2.,ox,oy,parent=smiley)  for _ in range(2)]
yeux[0].setPos(-b/6,-b/8)
yeux[1].setPos(+b/6,+b/8)
brush =QBrush(Qt.black)
for oiel in yeux:
	oiel.setBrush(brush)
	smiley.setPos(rectangleVerrt.mapToScene(rectangleVerrt.rect().center()))

	pass
smiley.setScale(1.5)
smiley.setRotation(20.)
smiley.setTranslation(10.0, 45)
smiley.setFlag(QGraphicsItem.ItemIsMovable)
scene.addItem(smiley)
texte= QGraphicsTextItem("Tous en scène ! ")
dy = rectangleVerrt.sceneBoundingRect().height()
texte.sceneBoundingRect().height()
texte.setPos(rectangleVerrt.x(),rectangleVerrt.y() +dy)
texte.setDefaultTextColor(QColor('blue'))

scene.addItem(texte)
#definition de la vue 
vue=QGraphicsView(scene)
vue.resize(800,600)
vue.fitInView(rectangleVerrt,Qt.KeepAspectRatio)

vue.show()
vue2 =  QGraphicsView(scene)
vue.setRenderHints(QPainter.Antialiasing)
vue2.resize(300,400)
vue2.rotate(-20)
vue2.show()
sys.exit(app.exec_())
