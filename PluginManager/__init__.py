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

from plugins.PluginManager.plugin_manager import Ui_PluginManager

import urllib2
import os
import zipfile

#for remove folder plugin
import shutil

plugin_name = "PluginManager"
plugin_create_menu = True
__all__ = {"PluginManager":1}


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
        #QMessageBox.information(None, plugin_name,'TEST', QMessageBox.Ok)
        global self, plugins, download_url
        self = pluginManagerUI()

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

    curr.setCheckState(QtCore.Qt.Checked)

    refresh_menuPlugin(iface)


def refresh_menuPlugin(session):

    # Clear all plugins
    session.menuPlugins.clear()
    # Restore all plugins
    session.plugins = session.get_plugins()
    session.populate_plugins_menu()

def btn_uninstalled():
    global self, plugins, download_url, iface
    f = open(os.getcwd() + '\\plugins\\PluginManager\\xmlfile2.txt', 'w')
    f.write(str(iface.plugins))
    f.close()

    iface.plugins = []
    curr = self.listWidget.currentIndex()
    current_index = curr.row()
    plugin_name = plugins[current_index]
    plugin_path = os.getcwd()+'\\plugins\\' + plugin_name
    # Remove plugin from path
    shutil.rmtree(plugin_path)

    curr.setCheckable(False)
    refresh_menuPlugin(session)
