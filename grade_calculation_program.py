# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'budur.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!


import sys
import os
import sqlite3
from PyQt5.QtWidgets import QWidget, QToolButton, QTabWidget, QApplication, QLabel, QPushButton, QHBoxLayout, \
    QVBoxLayout
from PyQt5.QtWidgets import QAction, qApp, QMainWindow, QLineEdit, QStatusBar,QMenu,QMenuBar
from PyQt5 import QtCore, QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1200, 560))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.donation_action = QAction("Support Turkey")
        self.menuHelp.addAction(self.donation_action)
        self.exit_action = QAction("Exit")
        self.exit_action.setShortcut("Ctrl+Q")
        self.menuHelp.addAction(self.exit_action)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.aqbilgi1 = QLabel("AQ1: ")
        self.aqbilgi2 = QLabel("AQ2: ")
        self.aqbilgi3 = QLabel("AQ3: ")
        self.aqbilgi4 = QLabel("AQ4: ")
        self.aqbilgi5 = QLabel("AQ5: ")
        self.aqbilgi6 = QLabel("AQ6: ")
        self.aqbilgi7 = QLabel("AQ7: ")
        self.aqbilgi8 = QLabel("AQ8: ")
        self.aqbilgi9 = QLabel("AQ9: ")
        self.aqbilgi10 = QLabel("AQ10: ")

        self.igbilgi1 = QLabel("IG1: ")
        self.igbilgi2 = QLabel("IG2: ")
        self.igbilgi3 = QLabel("IG3: ")
        self.igbilgi4 = QLabel("IG4: ")
        self.igbilgi5 = QLabel("IG5: ")
        self.mtbilgi1 = QLabel("MT1: ")
        self.mtbilgi2 = QLabel("MT2: ")
        self.mtbilgi3 = QLabel("MT3: ")
        self.mtbilgi4 = QLabel("MT4: ")
        self.mtbilgi5 = QLabel("MT5: ")
        self.pqbilgi1 = QLabel("PQ1: ")
        self.pqbilgi2 = QLabel("PQ2: ")
        self.pqbilgi3 = QLabel("PQ3: ")
        self.pqbilgi4 = QLabel("PQ4: ")
        self.pqbilgi5 = QLabel("PQ5: ")
        self.pqbilgi6 = QLabel("PQ6: ")
        self.pqbilgi7 = QLabel("PQ7: ")
        self.pqbilgi8 = QLabel("PQ8: ")
        self.pqbilgi9 = QLabel("PQ9: ")
        self.pqbilgi10 = QLabel("PQ10: ")

        self.sabilgi1 = QLabel("SA1:")
        self.sabilgi2 = QLabel("SA2:")
        self.sabilgi3 = QLabel("SA3:")
        self.sabilgi4 = QLabel("SA4:")
        self.sabilgi5 = QLabel("SA5:")

        self.aqbuton1 = QLineEdit()
        self.aqbuton2 = QLineEdit()
        self.aqbuton3 = QLineEdit()
        self.aqbuton4 = QLineEdit()
        self.aqbuton5 = QLineEdit()
        self.aqbuton6 = QLineEdit()
        self.aqbuton7 = QLineEdit()
        self.aqbuton8 = QLineEdit()
        self.aqbuton9 = QLineEdit()
        self.aqbuton10 = QLineEdit()

        self.igbuton1 = QLineEdit()
        self.igbuton2 = QLineEdit()
        self.igbuton3 = QLineEdit()
        self.igbuton4 = QLineEdit()
        self.igbuton5 = QLineEdit()
        self.mtbuton1 = QLineEdit()
        self.mtbuton2 = QLineEdit()
        self.mtbuton3 = QLineEdit()
        self.mtbuton4 = QLineEdit()
        self.mtbuton5 = QLineEdit()
        self.pqbuton1 = QLineEdit()
        self.pqbuton2 = QLineEdit()
        self.pqbuton3 = QLineEdit()
        self.pqbuton4 = QLineEdit()
        self.pqbuton5 = QLineEdit()
        self.pqbuton6 = QLineEdit()
        self.pqbuton7 = QLineEdit()
        self.pqbuton8 = QLineEdit()
        self.pqbuton9 = QLineEdit()
        self.pqbuton10 = QLineEdit()

        self.sabuton1 = QLineEdit()
        self.sabuton2 = QLineEdit()
        self.sabuton3 = QLineEdit()
        self.sabuton4 = QLineEdit()
        self.sabuton5 = QLineEdit()

        self.saqbilgi1 = QLabel("AQ1: ")
        self.saqbilgi2 = QLabel("AQ2: ")
        self.saqbilgi3 = QLabel("AQ3: ")
        self.saqbilgi4 = QLabel("AQ4: ")
        self.saqbilgi5 = QLabel("AQ5: ")
        self.saqbilgi6 = QLabel("AQ6: ")
        self.saqbilgi7 = QLabel("AQ7: ")
        self.saqbilgi8 = QLabel("AQ8: ")
        self.saqbilgi9 = QLabel("AQ9: ")
        self.saqbilgi10 = QLabel("AQ10: ")
        self.sigbilgi1 = QLabel("IG1: ")
        self.sigbilgi2 = QLabel("IG2: ")
        self.sigbilgi3 = QLabel("IG3: ")
        self.sigbilgi4 = QLabel("IG4: ")
        self.sigbilgi5 = QLabel("IG5: ")
        self.smtbilgi1 = QLabel("MT1: ")
        self.smtbilgi2 = QLabel("MT2: ")
        self.smtbilgi3 = QLabel("MT3: ")
        self.smtbilgi4 = QLabel("MT4: ")
        self.smtbilgi5 = QLabel("MT5: ")
        self.spqbilgi1 = QLabel("PQ1: ")
        self.spqbilgi2 = QLabel("PQ2: ")
        self.spqbilgi3 = QLabel("PQ3: ")
        self.spqbilgi4 = QLabel("PQ4: ")
        self.spqbilgi5 = QLabel("PQ5: ")
        self.spqbilgi6 = QLabel("PQ6: ")
        self.spqbilgi7 = QLabel("PQ7: ")
        self.spqbilgi8 = QLabel("PQ8: ")
        self.spqbilgi9 = QLabel("PQ9: ")
        self.spqbilgi10 = QLabel("PQ10: ")

        self.ssabilgi1 = QLabel("SA1:")
        self.ssabilgi2 = QLabel("SA2:")
        self.ssabilgi3 = QLabel("SA3:")
        self.ssabilgi4 = QLabel("SA4:")
        self.ssabilgi5 = QLabel("SA5:")

        self.saqbuton1 = QLineEdit()
        self.saqbuton2 = QLineEdit()
        self.saqbuton3 = QLineEdit()
        self.saqbuton4 = QLineEdit()
        self.saqbuton5 = QLineEdit()
        self.saqbuton6 = QLineEdit()
        self.saqbuton7 = QLineEdit()
        self.saqbuton8 = QLineEdit()
        self.saqbuton9 = QLineEdit()
        self.saqbuton10 = QLineEdit()
        self.sigbuton1 = QLineEdit()
        self.sigbuton2 = QLineEdit()
        self.sigbuton3 = QLineEdit()
        self.sigbuton4 = QLineEdit()
        self.sigbuton5 = QLineEdit()
        self.smtbuton1 = QLineEdit()
        self.smtbuton2 = QLineEdit()
        self.smtbuton3 = QLineEdit()
        self.smtbuton4 = QLineEdit()
        self.smtbuton5 = QLineEdit()
        self.spqbuton1 = QLineEdit()
        self.spqbuton2 = QLineEdit()
        self.spqbuton3 = QLineEdit()
        self.spqbuton4 = QLineEdit()
        self.spqbuton5 = QLineEdit()
        self.spqbuton6 = QLineEdit()
        self.spqbuton7 = QLineEdit()
        self.spqbuton8 = QLineEdit()
        self.spqbuton9 = QLineEdit()
        self.spqbuton10 = QLineEdit()

        self.ssabuton1 = QLineEdit()
        self.ssabuton2 = QLineEdit()
        self.ssabuton3 = QLineEdit()
        self.ssabuton4 = QLineEdit()
        self.ssabuton5 = QLineEdit()

        self.fall = QLabel("FALL")

        self.spring = QLabel("SPRING")
        self.altbilgi = QLabel("")
        self.temizlebuton = QPushButton("CLEAR GRADES")
        self.kaydetbuton = QPushButton("SAVE GRADES")
        self.achbuton = QPushButton("CALCULATE ACHIEVEMENT (FIRST TERM) AVERAGE")
        self.profbuton = QPushButton("CALCULATE PROFICIENCY (WHOLE YEAR) AVERAGE")
        self.altbilgi2 = QLabel("created by AliTunahanGüner")
        self.altbilgi3 = QLabel("2020 March")

        font = QtGui.QFont()
        font.setFamily("Laksaman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        self.altbilgi2.setFont(font)
        self.altbilgi3.setFont(font)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.altbilgi2.setPalette(palette)
        self.altbilgi3.setPalette(palette)
        self.fall.setPalette(palette)
        self.spring.setPalette(palette)

        palette2 = QtGui.QPalette()
        brush2 = QtGui.QBrush(QtGui.QColor(204, 0, 0))
        brush2.setStyle(QtCore.Qt.SolidPattern)
        palette2.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush2)
        brush2 = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush2.setStyle(QtCore.Qt.SolidPattern)
        palette2.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush2)
        brush2 = QtGui.QBrush(QtGui.QColor(204, 0, 0))
        brush2.setStyle(QtCore.Qt.SolidPattern)
        palette2.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush2)
        brush2 = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush2.setStyle(QtCore.Qt.SolidPattern)
        palette2.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush2)
        brush2 = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush2.setStyle(QtCore.Qt.SolidPattern)
        palette2.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush2)
        brush2 = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush2.setStyle(QtCore.Qt.SolidPattern)
        palette2.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush2)
        self.altbilgi.setPalette(palette2)

        h_box1 = QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.fall)
        h_box1.addStretch()

        h_box2 = QHBoxLayout()
        v_box1 = QVBoxLayout()
        v_box1.addWidget(self.aqbilgi1)
        v_box1.addWidget(self.aqbilgi2)
        v_box1.addWidget(self.aqbilgi3)
        v_box1.addWidget(self.aqbilgi4)
        v_box1.addWidget(self.aqbilgi5)
        v_box2 = QVBoxLayout()
        v_box2.addWidget(self.aqbuton1)
        v_box2.addWidget(self.aqbuton2)
        v_box2.addWidget(self.aqbuton3)
        v_box2.addWidget(self.aqbuton4)
        v_box2.addWidget(self.aqbuton5)
        v_box3 = QVBoxLayout()
        v_box3.addWidget(self.aqbilgi6)
        v_box3.addWidget(self.aqbilgi7)
        v_box3.addWidget(self.aqbilgi8)
        v_box3.addWidget(self.aqbilgi9)
        v_box3.addWidget(self.aqbilgi10)
        v_box4 = QVBoxLayout()
        v_box4.addWidget(self.aqbuton6)
        v_box4.addWidget(self.aqbuton7)
        v_box4.addWidget(self.aqbuton8)
        v_box4.addWidget(self.aqbuton9)
        v_box4.addWidget(self.aqbuton10)
        v_box5 = QVBoxLayout()
        v_box5.addWidget(self.igbilgi1)
        v_box5.addWidget(self.igbilgi2)
        v_box5.addWidget(self.igbilgi3)
        v_box5.addWidget(self.igbilgi4)
        v_box5.addWidget(self.igbilgi5)
        v_box6 = QVBoxLayout()
        v_box6.addWidget(self.igbuton1)
        v_box6.addWidget(self.igbuton2)
        v_box6.addWidget(self.igbuton3)
        v_box6.addWidget(self.igbuton4)
        v_box6.addWidget(self.igbuton5)
        v_box7 = QVBoxLayout()
        v_box7.addWidget(self.mtbilgi1)
        v_box7.addWidget(self.mtbilgi2)
        v_box7.addWidget(self.mtbilgi3)
        v_box7.addWidget(self.mtbilgi4)
        v_box7.addWidget(self.mtbilgi5)
        v_box8 = QVBoxLayout()
        v_box8.addWidget(self.mtbuton1)
        v_box8.addWidget(self.mtbuton2)
        v_box8.addWidget(self.mtbuton3)
        v_box8.addWidget(self.mtbuton4)
        v_box8.addWidget(self.mtbuton5)
        v_box9 = QVBoxLayout()
        v_box9.addWidget(self.pqbilgi1)
        v_box9.addWidget(self.pqbilgi2)
        v_box9.addWidget(self.pqbilgi3)
        v_box9.addWidget(self.pqbilgi4)
        v_box9.addWidget(self.pqbilgi5)
        v_box10 = QVBoxLayout()
        v_box10.addWidget(self.pqbuton1)
        v_box10.addWidget(self.pqbuton2)
        v_box10.addWidget(self.pqbuton3)
        v_box10.addWidget(self.pqbuton4)
        v_box10.addWidget(self.pqbuton5)
        v_box11 = QVBoxLayout()
        v_box11.addWidget(self.pqbilgi6)
        v_box11.addWidget(self.pqbilgi7)
        v_box11.addWidget(self.pqbilgi8)
        v_box11.addWidget(self.pqbilgi9)
        v_box11.addWidget(self.pqbilgi10)
        v_box12 = QVBoxLayout()
        v_box12.addWidget(self.pqbuton6)
        v_box12.addWidget(self.pqbuton7)
        v_box12.addWidget(self.pqbuton8)
        v_box12.addWidget(self.pqbuton9)
        v_box12.addWidget(self.pqbuton10)
        v_box13 = QVBoxLayout()
        v_box13.addWidget(self.sabilgi1)
        v_box13.addWidget(self.sabilgi2)
        v_box13.addWidget(self.sabilgi3)
        v_box13.addWidget(self.sabilgi4)
        v_box13.addWidget(self.sabilgi5)
        v_box14 = QVBoxLayout()
        v_box14.addWidget(self.sabuton1)
        v_box14.addWidget(self.sabuton2)
        v_box14.addWidget(self.sabuton3)
        v_box14.addWidget(self.sabuton4)
        v_box14.addWidget(self.sabuton5)

        h_box2.addLayout(v_box1)
        h_box2.addLayout(v_box2)
        h_box2.addLayout(v_box3)
        h_box2.addLayout(v_box4)
        h_box2.addLayout(v_box5)
        h_box2.addLayout(v_box6)
        h_box2.addLayout(v_box7)
        h_box2.addLayout(v_box8)
        h_box2.addLayout(v_box9)
        h_box2.addLayout(v_box10)
        h_box2.addLayout(v_box11)
        h_box2.addLayout(v_box12)
        h_box2.addLayout(v_box13)
        h_box2.addLayout(v_box14)

        h_box3 = QHBoxLayout()
        h_box3.addStretch()
        h_box3.addWidget(self.spring)
        h_box3.addStretch()

        h_box4 = QHBoxLayout()
        v_box15 = QVBoxLayout()
        v_box15.addWidget(self.saqbilgi1)
        v_box15.addWidget(self.saqbilgi2)
        v_box15.addWidget(self.saqbilgi3)
        v_box15.addWidget(self.saqbilgi4)
        v_box15.addWidget(self.saqbilgi5)
        v_box16 = QVBoxLayout()
        v_box16.addWidget(self.saqbuton1)
        v_box16.addWidget(self.saqbuton2)
        v_box16.addWidget(self.saqbuton3)
        v_box16.addWidget(self.saqbuton4)
        v_box16.addWidget(self.saqbuton5)
        v_box17 = QVBoxLayout()
        v_box17.addWidget(self.saqbilgi6)
        v_box17.addWidget(self.saqbilgi7)
        v_box17.addWidget(self.saqbilgi8)
        v_box17.addWidget(self.saqbilgi9)
        v_box17.addWidget(self.saqbilgi10)
        v_box18 = QVBoxLayout()
        v_box18.addWidget(self.saqbuton6)
        v_box18.addWidget(self.saqbuton7)
        v_box18.addWidget(self.saqbuton8)
        v_box18.addWidget(self.saqbuton9)
        v_box18.addWidget(self.saqbuton10)
        v_box19 = QVBoxLayout()
        v_box19.addWidget(self.sigbilgi1)
        v_box19.addWidget(self.sigbilgi2)
        v_box19.addWidget(self.sigbilgi3)
        v_box19.addWidget(self.sigbilgi4)
        v_box19.addWidget(self.sigbilgi5)
        v_box20 = QVBoxLayout()
        v_box20.addWidget(self.sigbuton1)
        v_box20.addWidget(self.sigbuton2)
        v_box20.addWidget(self.sigbuton3)
        v_box20.addWidget(self.sigbuton4)
        v_box20.addWidget(self.sigbuton5)
        v_box21 = QVBoxLayout()
        v_box21.addWidget(self.smtbilgi1)
        v_box21.addWidget(self.smtbilgi2)
        v_box21.addWidget(self.smtbilgi3)
        v_box21.addWidget(self.smtbilgi4)
        v_box21.addWidget(self.smtbilgi5)
        v_box22 = QVBoxLayout()
        v_box22.addWidget(self.smtbuton1)
        v_box22.addWidget(self.smtbuton2)
        v_box22.addWidget(self.smtbuton3)
        v_box22.addWidget(self.smtbuton4)
        v_box22.addWidget(self.smtbuton5)
        v_box23 = QVBoxLayout()
        v_box23.addWidget(self.spqbilgi1)
        v_box23.addWidget(self.spqbilgi2)
        v_box23.addWidget(self.spqbilgi3)
        v_box23.addWidget(self.spqbilgi4)
        v_box23.addWidget(self.spqbilgi5)
        v_box24 = QVBoxLayout()
        v_box24.addWidget(self.spqbuton1)
        v_box24.addWidget(self.spqbuton2)
        v_box24.addWidget(self.spqbuton3)
        v_box24.addWidget(self.spqbuton4)
        v_box24.addWidget(self.spqbuton5)
        v_box25 = QVBoxLayout()
        v_box25.addWidget(self.spqbilgi6)
        v_box25.addWidget(self.spqbilgi7)
        v_box25.addWidget(self.spqbilgi8)
        v_box25.addWidget(self.spqbilgi9)
        v_box25.addWidget(self.spqbilgi10)
        v_box26 = QVBoxLayout()
        v_box26.addWidget(self.spqbuton6)
        v_box26.addWidget(self.spqbuton7)
        v_box26.addWidget(self.spqbuton8)
        v_box26.addWidget(self.spqbuton9)
        v_box26.addWidget(self.spqbuton10)
        v_box27 = QVBoxLayout()
        v_box27.addWidget(self.ssabilgi1)
        v_box27.addWidget(self.ssabilgi2)
        v_box27.addWidget(self.ssabilgi3)
        v_box27.addWidget(self.ssabilgi4)
        v_box27.addWidget(self.ssabilgi5)
        v_box28 = QVBoxLayout()
        v_box28.addWidget(self.ssabuton1)
        v_box28.addWidget(self.ssabuton2)
        v_box28.addWidget(self.ssabuton3)
        v_box28.addWidget(self.ssabuton4)
        v_box28.addWidget(self.ssabuton5)

        h_box4.addLayout(v_box15)
        h_box4.addLayout(v_box16)
        h_box4.addLayout(v_box17)
        h_box4.addLayout(v_box18)
        h_box4.addLayout(v_box19)
        h_box4.addLayout(v_box20)
        h_box4.addLayout(v_box21)
        h_box4.addLayout(v_box22)
        h_box4.addLayout(v_box23)
        h_box4.addLayout(v_box24)
        h_box4.addLayout(v_box25)
        h_box4.addLayout(v_box26)
        h_box4.addLayout(v_box27)
        h_box4.addLayout(v_box28)

        h_box5 = QHBoxLayout()
        v_box29 = QVBoxLayout()
        v_box29.addWidget(self.kaydetbuton)
        v_box29.addWidget(self.temizlebuton)
        v_box30 = QVBoxLayout()
        v_box30.addWidget(QLabel(""))
        v_box31 = QVBoxLayout()
        v_box31.addWidget(self.achbuton)
        v_box31.addWidget(self.profbuton)
        h_box5.addLayout(v_box29)
        h_box5.addLayout(v_box30)
        h_box5.addLayout(v_box31)

        h_box6 = QHBoxLayout()
        h_box6.addStretch()
        h_box6.addWidget(self.altbilgi)
        h_box6.addStretch()

        h_box7 = QHBoxLayout()
        h_box7.addStretch()
        h_box7.addWidget(self.altbilgi2)
        h_box7.addStretch()

        h_box8 = QHBoxLayout()
        h_box8.addStretch()
        h_box8.addWidget(self.altbilgi3)
        h_box8.addStretch()

        v_box32 = QVBoxLayout()
        v_box32.addLayout(h_box7)
        v_box32.addLayout(h_box8)

        h_box9 = QHBoxLayout()
        h_box9.addStretch()
        h_box9.addLayout(v_box32)
        h_box9.addStretch()

        h_box10 = QHBoxLayout()
        h_box10.addWidget(QLabel(""))

        v_boxsuper = QVBoxLayout(self.tab)
        v_boxsuper.addLayout(h_box1)
        v_boxsuper.addLayout(h_box2)
        v_boxsuper.addLayout(h_box3)
        v_boxsuper.addLayout(h_box4)
        v_boxsuper.addLayout(h_box5)
        v_boxsuper.addLayout(h_box6)
        v_boxsuper.addLayout(h_box10)
        v_boxsuper.addLayout(h_box9)

        self.achbuton.clicked.connect(self.ach_calculate)
        self.profbuton.clicked.connect(self.prof_calculate)
        self.temizlebuton.clicked.connect(self.temizle)
        self.kaydetbuton.clicked.connect(self.notlari_guncelle)

        self.veritabani()
        bilgifall = QLabel("ACHIEVEMENT COEFFICIENTS")
        bilgifall.setPalette(palette2)
        bilgi_aqfall = QLabel("AQ FALL COEFFICIENT: ")
        bilgi_mtfall = QLabel("MT FALL COEFFICIENT: ")
        bilgi_pqfall = QLabel("PQ AND IG FALL COEFFICIENT: ")
        self.coe_aqfall = QLineEdit("0.125")
        self.coe_mtfall = QLineEdit("0.625")
        self.coe_pqfall = QLineEdit("0.25")

        bilgispring = QLabel("PROFICIENCY COEFFICIENTS")
        bilgispring.setPalette(palette2)
        bilgi_aqspring = QLabel("AQ SPRING COEFFICIENT: ")
        bilgi_mtspring = QLabel("MT SPRING COEFFICIENT: ")
        bilgi_pqspring = QLabel("PQ and IG SPRING COEFFICIENT: ")
        bilgi_saspring = QLabel("SA SPRING COEFFICIENT: ")

        bilgi_aqfall2 = QLabel("AQ FALL COEFFICIENT: ")
        bilgi_mtfall2 = QLabel("MT FALL COEFFICIENT: ")
        bilgi_pqfall2 = QLabel("PQ and IG FALL COEFFICIENT: ")
        bilgi_safall2 = QLabel("SA FALL COEFFICIENT: ")

        self.coe_aqspring = QLineEdit("0.05")
        self.coe_mtspring = QLineEdit("0.35")
        self.coe_pqspring = QLineEdit("0.10")
        self.coe_saspring = QLineEdit("0.05")

        self.coe_aqfall2 = QLineEdit("0.05")
        self.coe_mtfall2 = QLineEdit("0.25")
        self.coe_pqfall2 = QLineEdit("0.10")
        self.coe_safall2 = QLineEdit("0.05")

        h20_box1 = QHBoxLayout()
        h20_box1.addWidget(bilgifall)
        h20_box1.addStretch()
        h20_box1.addWidget(bilgispring)
        bos_element1 = QLabel("")
        bos_element2 = QLabel("")
        bos_element3 = QLabel("")
        bos_element4 = QLabel("")
        bos_element5 = QLabel("")
        bos_element6 = QLabel("")
        bos_element7 = QLabel("")
        bos_element8 = QLabel("")
        bos_element9 = QLabel("")
        bos_element10 = QLabel("")
        v20_box1 = QVBoxLayout()
        v20_box1.addWidget(bilgi_aqfall)
        v20_box1.addWidget(bilgi_mtfall)
        v20_box1.addWidget(bilgi_pqfall)
        v20_box1.addWidget(bos_element1)
        v20_box1.addWidget(bos_element2)
        v20_box1.addWidget(bos_element3)
        v20_box1.addWidget(bos_element4)
        v20_box1.addWidget(bos_element5)

        v20_box2 = QVBoxLayout()
        v20_box2.addWidget(self.coe_aqfall)
        v20_box2.addWidget(self.coe_mtfall)
        v20_box2.addWidget(self.coe_pqfall)
        v20_box2.addWidget(bos_element6)
        v20_box2.addWidget(bos_element7)
        v20_box2.addWidget(bos_element8)
        v20_box2.addWidget(bos_element9)
        v20_box2.addWidget(bos_element10)

        v20_box3 = QVBoxLayout()
        v20_box3.addWidget(bilgi_aqfall2)
        v20_box3.addWidget(bilgi_mtfall2)
        v20_box3.addWidget(bilgi_pqfall2)
        v20_box3.addWidget(bilgi_safall2)
        v20_box3.addWidget(bilgi_aqspring)
        v20_box3.addWidget(bilgi_mtspring)
        v20_box3.addWidget(bilgi_pqspring)
        v20_box3.addWidget(bilgi_saspring)

        v20_box4 = QVBoxLayout()
        v20_box4.addWidget(self.coe_aqfall2)
        v20_box4.addWidget(self.coe_mtfall2)
        v20_box4.addWidget(self.coe_pqfall2)
        v20_box4.addWidget(self.coe_safall2)
        v20_box4.addWidget(self.coe_aqspring)
        v20_box4.addWidget(self.coe_mtspring)
        v20_box4.addWidget(self.coe_pqspring)
        v20_box4.addWidget(self.coe_saspring)

        h20_box2 = QHBoxLayout()
        h20_box2.addLayout(v20_box1)
        h20_box2.addLayout(v20_box2)
        h20_box2.addStretch()
        h20_box2.addLayout(v20_box3)
        h20_box2.addLayout(v20_box4)

        h20_box3 = QHBoxLayout()
        self.clearbuton = QPushButton("CLEAR")
        self.formatbuton = QPushButton("FORMAT")


        v21_box1 = QVBoxLayout()
        v21_box1.addWidget(QLabel(""))
        v21_box2 = QVBoxLayout()
        v21_box2.addWidget(QLabel(""))
        v21_box3 = QVBoxLayout()
        v21_box3.addWidget(QLabel(""))



        v21_box4 = QVBoxLayout()
        v21_box4.addWidget(QLabel(""))



        v20_box6 = QVBoxLayout()
        v20_box6.addWidget(QLabel(""))
        v20_box6.addWidget(self.clearbuton)
        v20_box6.addWidget(self.formatbuton)

        h20_box3.addLayout(v21_box1)
        h20_box3.addLayout(v21_box2)
        h20_box3.addLayout(v21_box3)
        h20_box3.addLayout(v21_box4)
        h20_box3.addLayout(v20_box6)

        v20_box5 = QVBoxLayout(self.tab_2)
        v20_box5.addLayout(h20_box1)
        v20_box5.addLayout(h20_box2)
        v20_box5.addStretch()
        v20_box5.addLayout(h20_box3)

        self.clearbuton.clicked.connect(self.clearfunc)
        self.formatbuton.clicked.connect(self.formatfunc)
        self.donation_action.triggered.connect(self.donation)
        self.exit_action.triggered.connect(self.exit_fonc)
    def exit_fonc(self):
        qApp.quit()

    def donation(self):
        import tkinter as tk
        import webbrowser
        def callback(event):
            webbrowser.open_new(event.widget.cget("text"))
        x = "This program was written for the \n students who are studying in the\n Department of Basic English - METU.\nStudents can calculate their\nachievement and proficiency\navarage by using this program."

        root1 = tk.Tk()
        lbl3 = tk.Label(root1, text=x, fg="black", cursor="hand2")
        lbl3.pack(side="top")


        lbl2 = tk.Label(root1, text=r"MAKE A DONATION TO TÜRK KIZILAYI", fg="red", cursor="hand2")
        lbl2.pack(side="top")

        lbl = tk.Label(root1, text=r"https://www.kizilay.org.tr/Bagis/BagisYap/177/korona-gida-paketi-destegi", fg="blue", cursor="hand2")
        lbl.pack(side="top")

        logo = tk.PhotoImage(file="image.png")
        w1 = tk.Label(root1, image=logo).pack(side="bottom")

        lbl.bind("<Button-1>", callback)
        root1.wm_title("Support Turkey")
        root1.geometry("500x270+460+195")
        root1.mainloop()


    def clearfunc(self):
        self.coe_aqspring.clear()
        self.coe_mtspring.clear()
        self.coe_pqspring.clear()
        self.coe_saspring.clear()

        self.coe_aqfall.clear()
        self.coe_mtfall.clear()
        self.coe_pqfall.clear()

        self.coe_aqfall2.clear()
        self.coe_pqfall2.clear()
        self.coe_mtfall2.clear()
        self.coe_safall2.clear()


    def formatfunc(self):
        self.coe_aqspring.setText("0.05")
        self.coe_mtspring.setText("0.35")
        self.coe_pqspring.setText("0.10")
        self.coe_saspring.setText("0.05")
        self.coe_aqfall2.setText("0.05")
        self.coe_mtfall2.setText("0.25")
        self.coe_pqfall2.setText("0.10")
        self.coe_safall2.setText("0.05")

        self.coe_aqfall.setText("0.125")
        self.coe_mtfall.setText("0.625")
        self.coe_pqfall.setText("0.25")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GRADE CALCULATION PROGRAM"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Calculate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "About"))

    def ach_calculate(self):
        self.notlari_guncelle()
        liste_aq = list()
        liste_pq = list()
        liste_mt = list()
        liste_ig = list()

        a = 0
        b = 0
        c = 0
        d = 0
        while (a<10):
            a+=1
            liste_aq.append(eval("self.aqbuton{}.text()".format(a)))
        while (b<5):
            b+=1
            liste_mt.append(eval("self.mtbuton{}.text()".format(b)))
        while (c<5):
            c+=1
            liste_ig.append(eval("self.igbuton{}.text()".format(c)))
        while (d<10):
            d+=1
            liste_pq.append(eval("self.pqbuton{}.text()".format(d)))
        toplam_aq = 0
        toplam_pq = 0
        toplam_mt = 0
        toplam_ig = 0
        deger_aq = 0
        deger_pq = 0
        deger_mt = 0
        deger_ig = 0
        hata = 0
        for i in liste_aq:
            if (i!="" and i!="101"):
                try:
                    i = int(i)
                    toplam_aq += i
                    deger_aq += 1
                except:
                    hata += 1

        for i in liste_mt:
            if (i!="" and i!="101"):
                try:
                    i = int(i)
                    toplam_mt += i
                    deger_mt += 1
                except:
                    hata += 1
        for i in liste_pq:
            if (i!="" and i!="101"):
                try:
                    i = int(i)
                    toplam_pq += i
                    deger_pq += 1
                except:
                    hata += 1
        for i in liste_ig:
            if (i!="" and i!="101"):
                try:
                    i = int(i)
                    toplam_ig += i
                    deger_ig += 1
                except:
                    hata += 1
        if (hata != 0):
            self.altbilgi.setText("ERROR: ENTER GRADES PROPERLY")

        elif (deger_aq==0 or deger_mt==0 or deger_pq==0 or deger_ig==0):
            self.altbilgi.setText("ERROR: ENTER FALL GRADES")


        else:
            try:
                ortalama = (toplam_aq/deger_aq*float(self.coe_aqfall.text())) + (toplam_mt/deger_mt*float(self.coe_mtfall.text())) +((toplam_pq+toplam_ig)/(deger_pq+deger_ig)*float(self.coe_pqfall.text()))
                ortalama = round(ortalama, 5)
                ortalama = str(ortalama)
                ortalama = ortalama[:-1]
                ortalama = float(ortalama)
                self.altbilgi.setText("ACHIEVEMENT AVERAGE: {}".format(ortalama))
            except:
                self.altbilgi.setText("ERROR: ENTER ALL COEFFICIENTS")

    def prof_calculate(self):
        self.notlari_guncelle()
        liste_aq = list()
        liste_pq = list()
        liste_mt = list()
        liste_ig = list()
        liste_sa = list()

        liste_saq = list()
        liste_spq = list()
        liste_smt = list()
        liste_sig = list()
        liste_ssa = list()


        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        g = 0
        h = 0
        j = 0
        k = 0

        while (a<10):
            a+=1
            liste_aq.append(eval("self.aqbuton{}.text()".format(a)))
        while (b<5):
            b+=1
            liste_mt.append(eval("self.mtbuton{}.text()".format(b)))
        while (c<5):
            c+=1
            liste_ig.append(eval("self.igbuton{}.text()".format(c)))
        while (d<10):
            d+=1
            liste_pq.append(eval("self.pqbuton{}.text()".format(d)))
        while (e<5):
            e+=1
            liste_sa.append(eval("self.sabuton{}.text()".format(e)))

        while (f<10):
            f+=1
            liste_saq.append(eval("self.saqbuton{}.text()".format(f)))
        while (g<5):
            g+=1
            liste_smt.append(eval("self.smtbuton{}.text()".format(g)))
        while (h<5):
            h+=1
            liste_sig.append(eval("self.sigbuton{}.text()".format(h)))
        while (j<10):
            j+=1
            liste_spq.append(eval("self.spqbuton{}.text()".format(j)))
        while (k<5):
            k+=1
            liste_ssa.append(eval("self.ssabuton{}.text()".format(k)))

        toplam_aq = 0
        toplam_pq = 0
        toplam_mt = 0
        toplam_ig = 0
        toplam_sa = 0
        deger_aq = 0
        deger_pq = 0
        deger_mt = 0
        deger_ig = 0
        deger_sa = 0

        toplam_saq = 0
        toplam_spq = 0
        toplam_smt = 0
        toplam_sig = 0
        toplam_ssa = 0
        deger_saq = 0
        deger_spq = 0
        deger_smt = 0
        deger_sig = 0
        deger_ssa = 0
        hata = 0
        for i in liste_aq:
            if (i!="" and i!="101"):
                try:
                    i = int(i)
                    toplam_aq += i
                    deger_aq += 1
                except:
                    hata += 1

        for i in liste_mt:
            if (i!="" and i!="101"):
                try:
                    i = int(i)
                    toplam_mt += i
                    deger_mt += 1
                except:
                    hata += 1
        for i in liste_pq:
            if (i!="" and i!="101"):
                try:
                    i = int(i)
                    toplam_pq += i
                    deger_pq += 1
                except:
                    hata += 1
        for i in liste_ig:
            if (i!="" and i!="101"):
                try:
                    i = int(i)
                    toplam_ig += i
                    deger_ig += 1
                except:
                    hata += 1
        for i in liste_sa:
            if (i!="" and i!="101"):
                try:
                    i = int(i)
                    toplam_sa += i
                    deger_sa += 1
                except:
                    hata += 1


        for i in liste_saq:
            if (i!="" and i!="101"):
                try:
                    i = int(i)
                    toplam_saq += i
                    deger_saq += 1
                except:
                    hata += 1

        for i in liste_smt:
            if (i!="" and i!="101"):
                try:
                    i = int(i)
                    toplam_smt += i
                    deger_smt += 1
                except:
                    hata += 1
        for i in liste_spq:
            if (i!="" and i!="101"):
                try:
                    i = int(i)
                    toplam_spq += i
                    deger_spq += 1
                except:
                    hata += 1
        for i in liste_sig:
            if (i!="" and i!="101"):
                try:
                    i = int(i)
                    toplam_sig += i
                    deger_sig += 1
                except:
                    hata += 1
        for i in liste_ssa:
            if (i!="" and i!="101"):
                try:
                    i = int(i)
                    toplam_ssa += i
                    deger_ssa += 1
                except:
                    hata += 1
        if (hata != 0):
            self.altbilgi.setText("ERROR: ENTER GRADES PROPERLY")
        elif (deger_aq==0 or deger_mt==0 or deger_pq==0 or deger_ig==0 or deger_sa==0 or deger_saq==0 or deger_smt==0 or deger_spq==0 or deger_sig==0 or deger_ssa==0):
            self.altbilgi.setText("ERROR: ENTER WHOLE GRADES")

        else:

            try:
                mt_fall = (toplam_mt / deger_mt * float(self.coe_mtfall2.text()))
                aq_fall = (toplam_aq / deger_aq * float(self.coe_aqfall2.text()))
                sa_fall = (toplam_sa / deger_sa * float(self.coe_safall2.text()))
                ig_pq_fall = ((toplam_ig + toplam_pq) / (deger_ig + deger_pq) * float(self.coe_pqfall2.text()))

                mt_spring = (toplam_smt / deger_smt * float(self.coe_mtspring.text()))
                aq_spring = (toplam_saq / deger_saq * float(self.coe_aqspring.text()))
                sa_spring = (toplam_ssa / deger_ssa * float(self.coe_saspring.text()))
                ig_pq_spring = ((toplam_sig + toplam_spq) / (deger_sig + deger_spq) * float(self.coe_pqspring.text()))
                ortalama = mt_fall + aq_fall + sa_fall + ig_pq_fall + mt_spring + aq_spring +sa_spring +ig_pq_spring
                ortalama = round(ortalama, 5)
                ortalama = str(ortalama)
                ortalama = ortalama[:-1]
                ortalama = float(ortalama)
                self.altbilgi.setText("PROFICIENCY AVERAGE: {}".format(ortalama))
            except:
                self.altbilgi.setText("ERROR: ENTER ALL COEFFICIENTS")



    def temizle(self):
        a = 0
        while (a<10):
            a+=1
            b= "self.aqbuton{}.clear()".format(a)
            eval(b)
        a = 0
        while (a < 5):
            a += 1
            b = "self.mtbuton{}.clear()".format(a)
            eval(b)
        a = 0
        while (a < 10):
            a += 1
            b = "self.pqbuton{}.clear()".format(a)
            eval(b)
        a = 0
        while (a < 5):
            a += 1
            b = "self.igbuton{}.clear()".format(a)
            eval(b)
        a = 0
        while (a < 5):
            a += 1
            b = "self.sabuton{}.clear()".format(a)
            eval(b)
        a = 0
        while (a < 10):
            a += 1
            b = "self.saqbuton{}.clear()".format(a)
            eval(b)
        a = 0
        while (a < 5):
            a += 1
            b = "self.smtbuton{}.clear()".format(a)
            eval(b)
        a = 0
        while (a < 10):
            a += 1
            b = "self.spqbuton{}.clear()".format(a)
            eval(b)
        a = 0
        while (a < 5):
            a += 1
            b = "self.sigbuton{}.clear()".format(a)
            eval(b)
        a = 0
        while (a < 5):
            a += 1
            b = "self.ssabuton{}.clear()".format(a)
            eval(b)
        self.altbilgi.setText("")



    def veritabani(self):
        self.baglanti = sqlite3.connect("grades_saved.db")
        self.cursor = self.baglanti.cursor()

        sorgu = "CREATE TABLE IF NOT EXISTS grades (Type TEXT, Grade_1 FLO,Grade_2 FLO,Grade_3 FLO,Grade_4 FLO,Grade_5 FLO,Grade_6 FLO,Grade_7 FLO,Grade_8 FLO,Grade_9 FLO,Grade_10 FLO)"
        sorgu2 = "CREATE TABLE IF NOT EXISTS grades2 (Type TEXT, Grade_1 FLO,Grade_2 FLO,Grade_3 FLO,Grade_4 FLO,Grade_5 FLO)"
        self.cursor.execute(sorgu)
        self.cursor.execute(sorgu2)
        self.cursor.execute("SELECT * FROM grades")
        data_list1 = self.cursor.fetchall()
        self.cursor.execute("SELECT * FROM grades2")
        data_list2 = self.cursor.fetchall()
        if (len(data_list1)==0 and len(data_list2)==0):
            self.notlari_kaydet()
        self.first_function()
        self.baglanti.commit()

    def notlari_kaydet(self):
        sorgu = "INSERT INTO grades VALUES (?,?,?,?,?,?,?,?,?,?,?)"
        self.cursor.execute(sorgu,("AQ_FALL",self.aqbuton1.text(),self.aqbuton2.text(),self.aqbuton3.text(),self.aqbuton4.text(),self.aqbuton5.text(),self.aqbuton6.text(),self.aqbuton7.text(),self.aqbuton8.text(),self.aqbuton9.text(),self.aqbuton10.text()))
        self.cursor.execute(sorgu,("PQ_FALL",self.pqbuton1.text(),self.pqbuton2.text(),self.pqbuton3.text(),self.pqbuton4.text(),self.pqbuton5.text(),self.pqbuton6.text(),self.pqbuton7.text(),self.pqbuton8.text(),self.pqbuton9.text(),self.pqbuton10.text()))
        self.cursor.execute(sorgu,("AQ_SPRING",self.saqbuton1.text(),self.saqbuton2.text(),self.saqbuton3.text(),self.saqbuton4.text(),self.saqbuton5.text(),self.saqbuton6.text(),self.saqbuton7.text(),self.saqbuton8.text(),self.saqbuton9.text(),self.saqbuton10.text()))
        self.cursor.execute(sorgu,("PQ_SPRING",self.spqbuton1.text(),self.spqbuton2.text(),self.spqbuton3.text(),self.spqbuton4.text(),self.spqbuton5.text(),self.spqbuton6.text(),self.spqbuton7.text(),self.spqbuton8.text(),self.spqbuton9.text(),self.spqbuton10.text()))

        sorgu2 = "INSERT INTO grades2 VALUES (?,?,?,?,?,?)"
        self.cursor.execute(sorgu2,("IG_FALL",self.igbuton1.text(),self.igbuton2.text(),self.igbuton3.text(),self.igbuton4.text(),self.igbuton5.text()))
        self.cursor.execute(sorgu2,("MT_FALL",self.mtbuton1.text(),self.mtbuton2.text(),self.mtbuton3.text(),self.mtbuton4.text(),self.mtbuton5.text()))
        self.cursor.execute(sorgu2,("SA_FALL",self.sabuton1.text(),self.sabuton2.text(),self.sabuton3.text(),self.sabuton4.text(),self.sabuton5.text()))
        self.cursor.execute(sorgu2,("IG_SPRING",self.sigbuton1.text(),self.sigbuton2.text(),self.sigbuton3.text(),self.sigbuton4.text(),self.sigbuton5.text()))
        self.cursor.execute(sorgu2,("MT_SPRING",self.smtbuton1.text(),self.smtbuton2.text(),self.smtbuton3.text(),self.smtbuton4.text(),self.smtbuton5.text()))
        self.cursor.execute(sorgu2,("SA_SPRING",self.ssabuton1.text(),self.ssabuton2.text(),self.ssabuton3.text(),self.ssabuton4.text(),self.ssabuton5.text()))

        self.baglanti.commit()
    def notlari_guncelle(self):
        self.baglanti = sqlite3.connect("grades_saved.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "SELECT * FROM grades"
        self.cursor.execute(sorgu)
        aq = self.cursor.fetchall()
        a = 0
        while (a<10):
            a+=1
            grade = "self.aqbuton{}.text()".format(a)
            b = "AQ_FALL"
            sorgu2 = "Update grades set Grade_{}=? where Type=?".format(a)
            self.cursor.execute(sorgu2,(eval(grade),b))
        a = 0
        while (a < 10):
            a += 1
            grade = "self.pqbuton{}.text()".format(a)
            b = "PQ_FALL"
            sorgu2 = "Update grades set Grade_{}=? where Type=?".format(a)
            self.cursor.execute(sorgu2, (eval(grade), b))
        a = 0
        while (a < 5):
            a += 1
            grade = "self.mtbuton{}.text()".format(a)
            b = "MT_FALL"
            sorgu2 = "Update grades2 set Grade_{}=? where Type=?".format(a)
            self.cursor.execute(sorgu2, (eval(grade), b))
        a = 0
        while (a < 5):
            a += 1
            grade = "self.igbuton{}.text()".format(a)
            b = "IG_FALL"
            sorgu2 = "Update grades2 set Grade_{}=? where Type=?".format(a)
            self.cursor.execute(sorgu2, (eval(grade), b))
        a = 0
        while (a < 5):
            a += 1
            grade = "self.sabuton{}.text()".format(a)
            b = "SA_FALL"
            sorgu2 = "Update grades2 set Grade_{}=? where Type=?".format(a)
            self.cursor.execute(sorgu2, (eval(grade), b))

        a = 0
        while (a < 10):
            a += 1
            grade = "self.saqbuton{}.text()".format(a)
            b = "AQ_SPRING"
            sorgu2 = "Update grades set Grade_{}=? where Type=?".format(a)
            self.cursor.execute(sorgu2, (eval(grade), b))
        a = 0
        while (a < 10):
            a += 1
            grade = "self.spqbuton{}.text()".format(a)
            b = "PQ_SPRING"
            sorgu2 = "Update grades set Grade_{}=? where Type=?".format(a)
            self.cursor.execute(sorgu2, (eval(grade), b))
        a = 0
        while (a < 5):
            a += 1
            grade = "self.smtbuton{}.text()".format(a)
            b = "MT_SPRING"
            sorgu2 = "Update grades2 set Grade_{}=? where Type=?".format(a)
            self.cursor.execute(sorgu2, (eval(grade), b))
        a = 0
        while (a < 5):
            a += 1
            grade = "self.sigbuton{}.text()".format(a)
            b = "IG_SPRING"
            sorgu2 = "Update grades2 set Grade_{}=? where Type=?".format(a)
            self.cursor.execute(sorgu2, (eval(grade), b))
        a = 0
        while (a < 5):
            a += 1
            grade = "self.ssabuton{}.text()".format(a)
            b = "SA_SPRING"
            sorgu2 = "Update grades2 set Grade_{}=? where Type=?".format(a)
            self.cursor.execute(sorgu2, (eval(grade), b))
        self.altbilgi.setText("GRADES HAVE BEEN SAVED")
        self.baglanti.commit()
    def first_function(self):
        sorgu = "SELECT * FROM grades"
        self.cursor.execute(sorgu)
        grades_list = self.cursor.fetchall()
        sorgu2 = "SELECT * FROM grades2"
        self.cursor.execute(sorgu2)
        grades2_list = self.cursor.fetchall()

        aq_fall = grades_list[0]
        pq_fall = grades_list[1]
        aq_spring = grades_list[2]
        pq_spring = grades_list[3]

        ig_fall = grades2_list[0]
        mt_fall = grades2_list[1]
        sa_fall = grades2_list[2]
        ig_spring = grades2_list[3]
        mt_spring = grades2_list[4]
        sa_spring = grades2_list[5]
        a = 0
        while(a<10):
            a += 1
            eval("self.aqbuton{}.setText(str(aq_fall[a]))".format(a))
        a = 0
        while (a < 10):
            a += 1
            eval("self.pqbuton{}.setText(str(pq_fall[a]))".format(a))
        a = 0
        while (a < 10):
            a += 1
            eval("self.saqbuton{}.setText(str(aq_spring[a]))".format(a))
        a = 0
        while (a < 10):
            a += 1
            eval("self.spqbuton{}.setText(str(pq_spring[a]))".format(a))

        a = 0
        while (a < 5):
            a += 1
            eval("self.igbuton{}.setText(str(ig_fall[a]))".format(a))
        a = 0
        while (a < 5):
            a += 1
            eval("self.mtbuton{}.setText(str(mt_fall[a]))".format(a))
        a = 0
        while (a < 5):
            a += 1
            eval("self.sabuton{}.setText(str(sa_fall[a]))".format(a))
        a = 0
        while (a < 5):
            a += 1
            eval("self.sigbuton{}.setText(str(ig_spring[a]))".format(a))
        a = 0
        while (a < 5):
            a += 1
            eval("self.smtbuton{}.setText(str(mt_spring[a]))".format(a))
        a = 0
        while (a < 5):
            a += 1
            eval("self.ssabuton{}.setText(str(sa_spring[a]))".format(a))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

