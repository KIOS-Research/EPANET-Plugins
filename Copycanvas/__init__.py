# Name: Copycanvas
# Author: Marios S. Kyriakou, KIOS Research and Innovation Center of Excellence (KIOS CoE)
# Email: mariosmsk@gmail.com
# License: MIT

# This plugin works with EPANET MTP5r0:
# https://github.com/USEPA/SWMM-EPANET_User_Interface/releases/tag/MTP4r2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

plugin_name = "Copycanvas"
plugin_create_menu = True
__all__ = {"Copy canvas":1, "About":2}


def run(session=None, choice=None):

    def showMessage(title, msg, button):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QMessageBox.Ok)
        font = QtGui.QFont()
        font.setPointSize(9)
        msgBox.setFont(font)
        msgBox.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowCloseButtonHint)
        buttonY = msgBox.button(QMessageBox.Ok)
        buttonY.setText(button)
        buttonY.setFont(font)
        msgBox.exec_()

    ltopTitle = 'Plugin:Copycanvas'

    if choice is None:
        choice = 99
    if choice == 1:
        QtWidgets.QApplication.clipboard().setImage(QtGui.QImage(QtWidgets.QWidget.grab(session.canvas)))
        showMessage(title=ltopTitle, msg='Copied map canvas successfully.', button='OK')
    elif choice == 2:
        showMessage(title=ltopTitle, msg='This plugin created by Marios S. Kyriakou, KIOS Research '
                                         'and Innovation Center of Excellence (KIOS CoE). \n\nContact: mariosmsk@gmail.com', button='OK')