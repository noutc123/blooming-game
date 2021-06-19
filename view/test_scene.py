# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_scene.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
   
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(873, 646)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vuePrincipale = QtWidgets.QGraphicsView(self.centralwidget)
        self.vuePrincipale.setObjectName("vuePrincipale")
        self.horizontalLayout.addWidget(self.vuePrincipale)
        MainWindow.setCentralWidget(self.centralwidget)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonCreerDisque = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButtonCreerDisque.setObjectName("pushButtonCreerDisque")
        self.verticalLayout.addWidget(self.pushButtonCreerDisque)
        self.pushButtonChangerCouleur = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButtonChangerCouleur.setObjectName("pushButtonChangerCouleur")
        self.verticalLayout.addWidget(self.pushButtonChangerCouleur)
        self.lineEditTexte = QtWidgets.QLineEdit(self.dockWidgetContents_4)
        self.lineEditTexte.setObjectName("lineEditTexte")
        self.verticalLayout.addWidget(self.lineEditTexte)
        spacerItem = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.vueGlobale = QtWidgets.QGraphicsView(self.dockWidgetContents_4)
        self.vueGlobale.setObjectName("vueGlobale")
        self.verticalLayout.addWidget(self.vueGlobale)
        spacerItem1 = QtWidgets.QSpacerItem(20, 89, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.dialRotation = QtWidgets.QDial(self.dockWidgetContents_4)
        self.dialRotation.setMinimum(-180)
        self.dialRotation.setMaximum(180)
        self.dialRotation.setWrapping(True)
        self.dialRotation.setNotchTarget(30.0)
        self.dialRotation.setNotchesVisible(True)
        self.dialRotation.setObjectName("dialRotation")
        self.verticalLayout.addWidget(self.dialRotation)
        self.horizontalSliderZoom = QtWidgets.QSlider(self.dockWidgetContents_4)
        self.horizontalSliderZoom.setMinimum(10)
        self.horizontalSliderZoom.setMaximum(1000)
        self.horizontalSliderZoom.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderZoom.setObjectName("horizontalSliderZoom")
        self.verticalLayout.addWidget(self.horizontalSliderZoom)
        self.dockWidget.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Boîte à outils"))
        self.pushButtonCreerDisque.setText(_translate("MainWindow", "Créer disque"))

        self.pushButtonChangerCouleur.setText(_translate("MainWindow", "Changer Couleur"))

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.scene =QGraphicsScene()
        self.remplirScene()
        self.show()
        for vue in (self.vuePrincipale,self.vueGlobale):
            vue.setScene(self.scene)
            vue.setRenderHints(QPainter.Antialiasing)
            vue.fitInView(self.rectGris,Qt.KeepAspectRatio)
        self.vueGlobale.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.vueGlobale.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.vuePrincipale.setDragMode(QGraphicsView.RubberBandDrag)
        self.lineEditTexte.setText("Tous en scène !")
        self.angleVue = 0.0
        self.zoomPctVue = 1.0
        self.horizontalSliderZoom.setValue(100)
        self.showFullScreen()
    def remplirScene(self):
        scene = self.scene
        rectGris = scene.addRect(0,0,200,150,brush = QBrush(Qt.lightGray))
        self.rectGris = rectGris 
        self.texte = scene.addText("") 
        dy = rectGris.rect().height()
        self.texte.sceneBoundingRect().height() 
        self.texte.setPos(rectGris.x(),rectGris.y() + dy)
        self.texte.setDefaultTextColor(Qt.cyan) 
        scene.addItem(self.texte) 
        d = 48. # diametre smiley
        ox = 4. # largeur oeil 
        oy = 6. # hauteur oeil
        smiley = scene.addEllipse(-d/2,-d/2,d,d, brush=QBrush(Qt.yellow)) 
        yeux = [QGraphicsEllipseItem(-ox/2.,-oy/2.,ox,oy,parent=smiley)  for i in range(2)] 
        yeux[0].setPos(-d/6,-d/8)
        yeux[1].setPos(+d/6,-d/8)
        brush = QBrush(Qt.black) 
        for oeil in yeux:
            oeil.setBrush(brush) 
            smiley.setPos(rectGris.mapToScene(rectGris.rect().center()))
            smiley.setRotation(20)
            smiley.setScale(1.5)
            for item in scene.items():
                item.setFlag(QGraphicsItem.ItemIsMovable)
                item.setFlag(QGraphicsItem.ItemIsSelectable)
    @pyqtSlot()
    def on_pushButtonCreerDisque_clicked(self):
        disque = self.scene.addEllipse(0,0,20,20,brush=QBrush(Qt.white),pen=QPen(Qt.NoPen))
        disque.setFlag(QGraphicsItem.ItemIsMovable)
        disque.setFlag(QGraphicsItem.ItemIsSelectable)
        pass
    @pyqtSlot(str)
    def on_lineEditTexte_textChanged(self,msg):
        self.texte.setPlainText(msg)
        pass
    @pyqtSlot()
    def on_pushButtonChangerCouleur_clicked(self):
        itemsSelectionnes = self.scene.selectedItems()
        if len(itemsSelectionnes) > 0:
            couleurInit = itemsSelectionnes[0].brush().color()
            couleur = QColorDialog.getColor(couleurInit,self,'Changer la couleur')
            if couleur.isValid():
                brosse = QBrush(couleur)
            for item in itemsSelectionnes:
                item.setBrush(brosse)
    @pyqtSlot(int)
    def on_dialRotation_valueChanged(self,nouvelAngleVue):
        self.vuePrincipale.rotate(nouvelAngleVue-self.angleVue)
        self.angleVue = nouvelAngleVue
    @pyqtSlot(int)
    def on_horizontalSliderZoom_valueChanged(self,nouvZoomPctVue):
        f = (nouvZoomPctVue/100.0) / self.zoomPctVue
        self.vuePrincipale.scale(f,f)
        self.zoomPctVue = nouvZoomPctVue/100.0
if __name__ == '__main__': 
    app= QApplication(sys.argv)
    mainWindow = MainWindow() 
    sys.exit(app.exec_())