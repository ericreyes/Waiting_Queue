# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WQ.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from math import factorial
from Tkinter import *
import time



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
        MainWindow.resize(1182, 889)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.InputMiu = QtGui.QLineEdit(self.centralwidget)
        self.InputMiu.setGeometry(QtCore.QRect(100, 94, 121, 31))

        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.InputMiu.setFont(font)
        self.InputMiu.setMouseTracking(True)
        self.InputMiu.setAutoFillBackground(False)
        self.InputMiu.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.InputMiu.setText(_fromUtf8(""))
        self.InputMiu.setObjectName(_fromUtf8("InputMiu"))
        self.InputMiu.setInputMask('999999999')
        self.miu = QtGui.QLabel(self.centralwidget)
        self.miu.setEnabled(True)
        self.miu.setGeometry(QtCore.QRect(50, 100, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.miu.setFont(font)
        self.miu.setObjectName(_fromUtf8("miu"))
        self.miu_2 = QtGui.QLabel(self.centralwidget)
        self.miu_2.setEnabled(True)
        self.miu_2.setGeometry(QtCore.QRect(40, 196, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.miu_2.setFont(font)
        self.miu_2.setObjectName(_fromUtf8("miu_2"))
        self.InputLambda = QtGui.QLineEdit(self.centralwidget)
        self.InputLambda.setGeometry(QtCore.QRect(90, 190, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.InputLambda.setFont(font)
        self.InputLambda.setMouseTracking(True)
        self.InputLambda.setText(_fromUtf8(""))
        self.InputLambda.setObjectName(_fromUtf8("InputLambda"))
        self.InputLambda.setInputMask('999999999')
        self.miu_3 = QtGui.QLabel(self.centralwidget)
        self.miu_3.setEnabled(True)
        self.miu_3.setGeometry(QtCore.QRect(40, 316, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.miu_3.setFont(font)
        self.miu_3.setObjectName(_fromUtf8("miu_3"))
        self.InputServers = QtGui.QLineEdit(self.centralwidget)
        self.InputServers.setGeometry(QtCore.QRect(90, 310, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.InputServers.setFont(font)
        self.InputServers.setMouseTracking(True)
        self.InputServers.setText(_fromUtf8(""))
        self.InputServers.setObjectName(_fromUtf8("InputServers"))
        self.InputServers.setInputMask('999')
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.botonCalcular = QtGui.QPushButton(self.centralwidget)
        self.botonCalcular.setGeometry(QtCore.QRect(80, 430, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.botonCalcular.setFont(font)
        self.botonCalcular.setObjectName(_fromUtf8("botonCalcular"))
        self.botonCalcular.clicked.connect(self.calculate_data)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 620, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.outputP0 = QtGui.QTextBrowser(self.centralwidget)
        self.outputP0.setGeometry(QtCore.QRect(230, 610, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.outputP0.setFont(font)
        self.outputP0.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.outputP0.setMouseTracking(False)
        self.outputP0.setObjectName(_fromUtf8("outputP0"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 630, 66, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.outputL = QtGui.QTextBrowser(self.centralwidget)
        self.outputL.setGeometry(QtCore.QRect(230, 700, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.outputL.setFont(font)
        self.outputL.setObjectName(_fromUtf8("outputL"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 710, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.outputW = QtGui.QTextBrowser(self.centralwidget)
        self.outputW.setGeometry(QtCore.QRect(230, 780, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.outputW.setFont(font)
        self.outputW.setObjectName(_fromUtf8("outputW"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 790, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(490, 630, 66, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.outputLq = QtGui.QTextBrowser(self.centralwidget)
        self.outputLq.setGeometry(QtCore.QRect(540, 610, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.outputLq.setFont(font)
        self.outputLq.setObjectName(_fromUtf8("outputLq"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(470, 620, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(500, 710, 66, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.outputWq = QtGui.QTextBrowser(self.centralwidget)
        self.outputWq.setGeometry(QtCore.QRect(540, 690, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.outputWq.setFont(font)
        self.outputWq.setObjectName(_fromUtf8("outputWq"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(460, 700, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.outputRO = QtGui.QTextBrowser(self.centralwidget)
        self.outputRO.setGeometry(QtCore.QRect(540, 770, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.outputRO.setFont(font)
        self.outputRO.setObjectName(_fromUtf8("outputRO"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(470, 770, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 780, 66, 17))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(590, 20, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.errorLabel = QtGui.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(440, 470, 461, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 16, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 118, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 67, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 8, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 10, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 16, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 135, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 16, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 118, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 67, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 8, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 10, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 16, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 135, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 8, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 16, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 118, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 67, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 8, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 10, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 8, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 8, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 16, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 16, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 16, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.errorLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.errorLabel.setFont(font)
        self.errorLabel.setTextFormat(QtCore.Qt.AutoText)
        self.errorLabel.setObjectName(_fromUtf8("errorLabel"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 550, 1181, 20))
        self.line.setBaseSize(QtCore.QSize(3, 3))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(353, 0, 20, 561))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.botonReset = QtGui.QPushButton(self.centralwidget)
        self.botonReset.setGeometry(QtCore.QRect(870, 660, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.botonReset.setFont(font)
        self.botonReset.setObjectName(_fromUtf8("botonReset"))
        self.botonReset.clicked.connect(self.reset_values)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 540, 1181, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(340, 10, 20, 551))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1182, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulación de linea de espera", None))
        self.miu.setText(_translate("MainWindow", "μ = ", None))
        self.miu_2.setText(_translate("MainWindow", "λ =", None))
        self.miu_3.setText(_translate("MainWindow", "D =", None))
        self.label.setText(_translate("MainWindow", "Cada 1 segundo , es 1 minuto.", None))
        self.botonCalcular.setText(_translate("MainWindow", "Iniciar Simulación", None))
        self.label_2.setText(_translate("MainWindow", " P   =", None))
        self.outputP0.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:18pt; font-weight:600; font-style:italic;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "0", None))
        self.outputL.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:18pt; font-weight:600; font-style:italic;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", " L =", None))
        self.outputW.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:18pt; font-weight:600; font-style:italic;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>", None))
        self.label_7.setText(_translate("MainWindow", " W  =", None))
        self.label_8.setText(_translate("MainWindow", "q", None))
        self.outputLq.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:18pt; font-weight:600; font-style:italic;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>", None))
        self.label_9.setText(_translate("MainWindow", " L   =", None))
        self.label_10.setText(_translate("MainWindow", "q", None))
        self.outputWq.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:18pt; font-weight:600; font-style:italic;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>", None))
        self.label_11.setText(_translate("MainWindow", " W   =", None))
        self.outputRO.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:18pt; font-weight:600; font-style:italic;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>", None))
        self.label_13.setText(_translate("MainWindow", "ρ\n"
"  ", None))
        self.label_4.setText(_translate("MainWindow", "=", None))
        self.label_6.setText(_translate("MainWindow", "Simulación de sistema", None))
        self.errorLabel.setText(_translate("MainWindow", "", None))  ##ERROR ESCONDIDO
        self.botonReset.setText(_translate("MainWindow", "Reset", None))





    '''
    ############################################################################################################
    GENERADO POR LA HERRAMIENTA!    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ############################################################################################################
    '''


    #Funciones de la clase::::


    def start_time():
        # sera de la manera que manipulemos el tiempo
        pass

    def clear_board(self,MainWindow):
        # Eliminar las figuras credas
        pass
    def reset_values(self, MainWindow):
        self.outputP0.setText('')
        self.outputL.setText('')
        self.outputW.setText('')
        self.outputLq.setText('')
        self.outputWq.setText('')
        self.outputRO.setText('')

        self.InputLambda.setText('')
        self.InputMiu.setText('')
        self.InputServers.setText('')
        #self.clear_board()
        # TODO: Agregar funciones o destruir objetos de figura

    def calculate_data(self, MainWindow):
        miu = float(self.InputMiu.text())
        my_lambda = float(self.InputLambda.text())
        m_servers = int(self.InputServers.text())
        inqueue = 0
        serving = 0
        #Sumatoria para formula de P0
        sumatoria = 0


        for n in xrange(0, m_servers):
            sumatoria = sumatoria + (1.0 / factorial(n)) * (my_lambda/miu)**n
        print sumatoria
        #Formulas!

        #TODO check P0!!!!
        P0 = 1.0/( sumatoria + (1.0 / factorial(m_servers)) * ((my_lambda / miu) ** m_servers) * ((m_servers*miu)/((m_servers*miu) - my_lambda)))

        L = (my_lambda * miu *(my_lambda/miu)**m_servers) / (factorial(m_servers-1) * (m_servers*miu - my_lambda)**2) * P0 + my_lambda/miu

        W =  L / my_lambda

        Lq = L - my_lambda/miu

        Wq = W - 1/miu

        RO = my_lambda/(m_servers* miu)


        self.outputP0.setText(str(P0))
        self.outputL.setText(str(L))
        self.outputW.setText(str(W))
        self.outputLq.setText(str(Lq))
        self.outputWq.setText(str(Wq))
        self.outputRO.setText(str(RO))

        root.after(2000, update_values(my_lambda,miu,m_servers, inqueue, serving))



    #def set_error_label():
    #     if not self.InputMiu.hasAcceptableInput(self):
    #         errorLabel.setText("Reescriba Miu")
    #     if not self.InputLambda.hasAcceptableInput:
    #         errorLabel.setText("Reescriba Lambda")
    #     if not self.InputMiu.hasAcceptableInput(self) and not self.InputLambda.hasAcceptableInput(self):
    #         errorLabel.setText("Reescriba Miu y lambda, solo numeros")

root = Tk()
canvas = Canvas(root, width=500, height=500)
root.withdraw()


#root.after(500, add_letter)

def update_values(my_lambda,miu,m_servers, inqueue, serving):

    while True:
        # Inqueue
        inqueue += my_lambda
        root.after(100,canvas_figuras(inqueue, serving))
        inqueue -= (miu * m_servers)
        root.after(100,canvas_figuras(inqueue, serving))

        # Serving
        serving += miu
        root.after(100,canvas_figuras(inqueue, serving))
        serving -= miu * m_servers
        root.after(100,canvas_figuras(inqueue, serving))


    # Llamar queue_clientes con nuevos valores

def canvas_figuras(inqueue, serving):
    root.deiconify()
    canvas.create_line(125,255,300,255, width="3", arrow="last")
    canvas.create_rectangle(350,100,400,150)
    canvas.create_rectangle(350,350,400,400)
    if inqueue < 0:
        inqueue = 0
    rect = canvas.create_rectangle(10,275,75,275-inqueue, fill="green", tags="Lista")
    if inqueue >= 20 and inqueue <= 74:
        canvas.itemconfig(rect, fill="yellow")
    else:
        if inqueue >= 75:
            canvas.itemconfig(rect, fill="red")

    for i in xrange(0,1):
        x1 = 70
        y1 = 240
        x2 = 90
        y2 = 270
        oval = canvas.create_oval(x1,y1,x2,y2, fill="blue", tags="Persona")
        for j in xrange(0,20):
            x1 +=10
            x2 +=10
            canvas.coords(oval,x1, y1, x2, y2)
            time.sleep(0.05)
            root.update()
            canvas.pack()
        canvas.delete("Persona")
        canvas.delete("Lista")
        #txt.set('hols')
        canvas.pack()
        root.update()
        time.sleep(0.1)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
