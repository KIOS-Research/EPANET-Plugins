# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plugin_manager.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PluginManager(object):
    def setupUi(self, PluginManager):
        PluginManager.setObjectName("PluginManager")
        PluginManager.resize(645, 528)
        PluginManager.setMinimumSize(QtCore.QSize(645, 528))
        PluginManager.setMaximumSize(QtCore.QSize(645, 528))
        self.install_re = QtWidgets.QPushButton(PluginManager)
        self.install_re.setGeometry(QtCore.QRect(390, 470, 101, 41))
        self.install_re.setObjectName("install_re")
        self.uninstall = QtWidgets.QPushButton(PluginManager)
        self.uninstall.setGeometry(QtCore.QRect(520, 470, 101, 41))
        self.uninstall.setObjectName("uninstall")
        self.listWidget = QtWidgets.QListWidget(PluginManager)
        self.listWidget.setGeometry(QtCore.QRect(20, 20, 221, 431))
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listWidget.setObjectName("listWidget")
        self.textEdit = QtWidgets.QTextEdit(PluginManager)
        self.textEdit.setGeometry(QtCore.QRect(250, 20, 371, 431))
        self.textEdit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(PluginManager)
        QtCore.QMetaObject.connectSlotsByName(PluginManager)

    def retranslateUi(self, PluginManager):
        _translate = QtCore.QCoreApplication.translate
        PluginManager.setWindowTitle(_translate("PluginManager", "Form"))
        self.install_re.setText(_translate("PluginManager", "Install"))
        self.uninstall.setText(_translate("PluginManager", "Uninstall"))
        self.textEdit.setHtml(_translate("PluginManager", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Plugin Name:</span><span style=\" font-family:\'Courier New\'; font-size:8pt; color:#000000; background-color:#ffffff;\"> FireFlow</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Version    :</span><span style=\" font-family:\'Courier New\'; font-size:8pt; color:#000000; background-color:#ffffff;\"> 0.1</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Description:</span><span style=\" font-family:\'Courier New\'; font-size:8pt; color:#000000; background-color:#ffffff;\"> Fire Flow Calculations Software</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">About      :</span><span style=\" font-family:\'Courier New\'; font-size:8pt; color:#000000; background-color:#ffffff;\"> FireFlow is a Freeware, EPANET based tool, which will calculate the available flow at network junctions while a minimal pressure is kept at demand junctions. FireFlow can run in a “Steady State” mode or perform an “Extended Period Simulation” (EPS). Using the EPS mode you can find how long can a specified flow be delivered? Or, what is the maximal flow that can be delivered for a specified period?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Homepage   :</span><span style=\" font-family:\'Courier New\'; font-size:8pt; color:#000000; background-color:#ffffff;\"> </span><span style=\" font-size:8pt; color:#0000ff;\">http://www.optiwater.com/fireflow/</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Author     :</span><span style=\" font-family:\'Courier New\'; font-size:8pt; color:#000000; background-color:#ffffff;\"> Elad Salomons</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Download   : </span><span style=\" font-size:8pt; color:#0000ff;\">https://github.com/KIOS-Research/EPANET-Plugins/blob/dev/FireFlow.zip</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Uploaded by: </span><span style=\" font-family:\'Courier New\'; font-size:8pt; color:#000000; background-color:#ffffff;\">eladsad</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Tracker    : </span><span style=\" font-size:8pt; color:#0000ff;\">https://github.com/eladsal/EPANET-Plugins/issues/</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Repository : </span><span style=\" font-size:8pt; color:#0000ff;\">https://github.com/eladsal/EPANET-Plugins/</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Tags       : </span><span style=\" font-family:\'Courier New\'; font-size:8pt; color:#000000; background-color:#ffffff;\">fireflow, pressure</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000;\"><br /></p></body></html>"))


