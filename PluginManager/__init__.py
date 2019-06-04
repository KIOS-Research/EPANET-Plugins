# Name: PluginManager
# Author: Marios S. Kyriakou, Demetrios G. Eliades, KIOS Research and Innovation Center of Excellence (KIOS CoE)
# Email: mariosmsk@gmail.com
# License: MIT

# This plugin works with EPANET MTP4r2:
# https://github.com/USEPA/SWMM-EPANET_User_Interface/releases/tag/MTP4r2

try:
    from PyQt4 import QtCore, QtGui
    from PyQt4.QtGui import QMessageBox
except:
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtWidgets import QMessageBox

import urllib2
import os
import zipfile
import inspect, sys
plugin_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(plugin_dir)
from plugin_manager import Ui_PluginManager

#for remove folder plugin
import shutil

plugin_name = "PluginManager"
plugin_create_menu = True
__all__ = {"Manage and Install Plugins...":1}


class pluginManagerUI(QtGui.QDialog, Ui_PluginManager):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

def run(session=None, choice=None):
    # save session
    save_session(session)

    # Read xml file from github repo #Because not need pip install something
    # check code again for updates
    file = urllib2.urlopen('https://raw.githubusercontent.com/KIOS-Research/EPANET-Plugins/dev/plugin_repo.xml')
    data = file.read()
    file.close()

    # Get all plugins from repository plugins
    plugins = []
    download_url = []
    for line in data.split('\n'):
        param = 'name'
        if param in line:
            try:
                plug = line[line.index(param)+len(param)+2:line.index('version')-2]
                plugins.append(plug)
            except:
                pass
        param2 = '<download_url>'
        if param2 in line:
            download_url.append('https://raw.githubusercontent.com/KIOS-Research/EPANET-Plugins/dev/'+plug + '.zip')#(line[line.index(param2)+len(param2):line.index('</download_url>')])
            # https://raw.githubusercontent.com/KIOS-Research/EPANET-Plugins/dev/Copycanvas.zip #plugin name only

    # Check if plugin
    if choice is None:
        choice = 99
    if choice == 1:
        global self, plugins, download_url
        self = pluginManagerUI()
        self.setWindowTitle('Manage and Install Plugins...')

        for plugin in plugins:
            item = QtGui.QListWidgetItem()
            item.setText(plugin)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.listWidget.addItem(item)

        ##self.listWidget.clicked.connect(download_url_zip)
        self.install_re.clicked.connect(btn_installed)
        self.uninstall.clicked.connect(btn_uninstalled)
        self.show()

        b # error to show ui

def save_session(session):
    global iface
    iface = session

def btn_installed():
    global self, plugins, download_url, iface

    curr = self.listWidget.currentIndex()
    current_index = curr.row()
    url = download_url[current_index]

    # Download and unzip zip file of plugin, then remove zip
    f = urllib2.urlopen(url)
    zipFilePath = os.getcwd()+'\\plugins\\' + os.path.basename(url)
    zipFile = open(zipFilePath, "wb")
    zipFile.write(f.read())
    zipFile.close()
    f.close()
    zip_ref = zipfile.ZipFile(zipFilePath, 'r')
    zip_ref.extractall(os.getcwd()+'\\plugins\\')
    zip_ref.close()
    os.remove(zipFilePath)

    self.listWidget.item(current_index).setCheckState(QtCore.Qt.Checked)

    refresh_menuPlugin(iface)


def refresh_menuPlugin(session):

    # Clear all plugins
    session.menuPlugins.clear()
    # Restore all plugins
    session.plugins = session.get_plugins()
    session.populate_plugins_menu()

def btn_uninstalled():
    global self, plugins, download_url, iface

    curr = self.listWidget.currentIndex()
    current_index = curr.row()
    plugin_name = plugins[current_index]

    reply = QMessageBox.question(None, 'EPANET Python Plugin Installer',
                                 'Are you sure you want to uninstall the following plugin?\n'+'('+plugin_name+')',
                                 QMessageBox.Yes | QMessageBox.No)


    if reply == QMessageBox.Yes:

        plugin_path = os.getcwd()+'\\plugins\\' + plugin_name
        # Clear all plugins
        iface.menuPlugins.clear()

        # Remove plugin from path
        shutil.rmtree(plugin_path)
        QMessageBox.information(None, plugin_name,'Plugin uninstalled successfully.', QMessageBox.Ok)