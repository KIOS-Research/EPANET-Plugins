# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmFireFlow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_frmFireFlow(object):
    def setupUi(self, frmFireFlow):
        frmFireFlow.setObjectName(_fromUtf8("frmFireFlow"))
        frmFireFlow.resize(1047, 712)
        self.centralWidget = QtGui.QWidget(frmFireFlow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.cmdRun = QtGui.QPushButton(self.centralWidget)
        self.cmdRun.setGeometry(QtCore.QRect(250, 570, 151, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cmdRun.setFont(font)
        self.cmdRun.setObjectName(_fromUtf8("cmdRun"))
        self.lstJunctions = QtGui.QListWidget(self.centralWidget)
        self.lstJunctions.setGeometry(QtCore.QRect(20, 50, 141, 331))
        self.lstJunctions.setObjectName(_fromUtf8("lstJunctions"))
        self.mplwindow = QtGui.QWidget(self.centralWidget)
        self.mplwindow.setGeometry(QtCore.QRect(170, 20, 851, 501))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow.sizePolicy().hasHeightForWidth())
        self.mplwindow.setSizePolicy(sizePolicy)
        self.mplwindow.setAutoFillBackground(False)
        self.mplwindow.setObjectName(_fromUtf8("mplwindow"))
        self.mplvl = QtGui.QVBoxLayout(self.mplwindow)
        self.mplvl.setMargin(11)
        self.mplvl.setSpacing(6)
        self.mplvl.setObjectName(_fromUtf8("mplvl"))
        self.line = QtGui.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(170, 520, 851, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.txtFromDemand = QtGui.QPlainTextEdit(self.centralWidget)
        self.txtFromDemand.setGeometry(QtCore.QRect(170, 570, 61, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtFromDemand.setFont(font)
        self.txtFromDemand.setMouseTracking(False)
        self.txtFromDemand.setObjectName(_fromUtf8("txtFromDemand"))
        self.txtToDemand = QtGui.QPlainTextEdit(self.centralWidget)
        self.txtToDemand.setGeometry(QtCore.QRect(170, 650, 61, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtToDemand.setFont(font)
        self.txtToDemand.setMouseTracking(False)
        self.txtToDemand.setObjectName(_fromUtf8("txtToDemand"))
        self.txtDeltaDemand = QtGui.QPlainTextEdit(self.centralWidget)
        self.txtDeltaDemand.setGeometry(QtCore.QRect(170, 610, 61, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtDeltaDemand.setFont(font)
        self.txtDeltaDemand.setMouseTracking(False)
        self.txtDeltaDemand.setMidLineWidth(0)
        self.txtDeltaDemand.setObjectName(_fromUtf8("txtDeltaDemand"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(20, 570, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(20, 610, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(20, 650, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        frmFireFlow.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(frmFireFlow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        frmFireFlow.setStatusBar(self.statusBar)

        self.retranslateUi(frmFireFlow)
        QtCore.QMetaObject.connectSlotsByName(frmFireFlow)

    def retranslateUi(self, frmFireFlow):
        frmFireFlow.setWindowTitle(_translate("frmFireFlow", "FireFlow plugin for EPANET", None))
        self.cmdRun.setText(_translate("frmFireFlow", "Run ", None))
        self.txtFromDemand.setPlainText(_translate("frmFireFlow", "0", None))
        self.txtToDemand.setPlainText(_translate("frmFireFlow", "1200", None))
        self.txtDeltaDemand.setPlainText(_translate("frmFireFlow", "60", None))
        self.label.setText(_translate("frmFireFlow", "Junctions:", None))
        self.label_2.setText(_translate("frmFireFlow", "Minimum demand:", None))
        self.label_3.setText(_translate("frmFireFlow", "Demand step:", None))
        self.label_4.setText(_translate("frmFireFlow", "Maximum demand:", None))
