# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plugin_manager.ui'
#
# Created by: PyQt4 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


class Ui_PluginManager(object):
    def setupUi(self, PluginManager):
        PluginManager.setObjectName("PluginManager")
        PluginManager.resize(645, 528)
        self.install_re = QtGui.QPushButton(PluginManager)
        self.install_re.setGeometry(QtCore.QRect(390, 470, 101, 41))
        self.install_re.setObjectName("install_re")
        self.uninstall = QtGui.QPushButton(PluginManager)
        self.uninstall.setGeometry(QtCore.QRect(520, 470, 101, 41))
        self.uninstall.setObjectName("uninstall")
        self.listWidget = QtGui.QListWidget(PluginManager)
        self.listWidget.setGeometry(QtCore.QRect(20, 20, 221, 431))
        self.listWidget.setObjectName("listWidget")
        self.webView = QWebView(PluginManager)
        self.webView.setGeometry(QtCore.QRect(250, 20, 371, 431))
        self.webView.setUrl(QtCore.QUrl("https://raw.githubusercontent.com/KIOS-Research/EPANET-Plugins/dev/plugin_repo.xml"))
        self.webView.setObjectName("webView")

        self.retranslateUi(PluginManager)
        QtCore.QMetaObject.connectSlotsByName(PluginManager)

    def retranslateUi(self, PluginManager):
        _translate = QtCore.QCoreApplication.translate
        PluginManager.setWindowTitle(_translate("PluginManager", "Form"))
        self.install_re.setText(_translate("PluginManager", "Install"))
        self.uninstall.setText(_translate("PluginManager", "Uninstall"))


from PyQt4.QtWebKit import QWebView