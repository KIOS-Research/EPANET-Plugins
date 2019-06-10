# -*- coding: utf-8 -*-

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

from xml.dom import minidom

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

    # parse xml file #get all plugins
    doc = minidom.parseString(data)
    getPlugins = doc.documentElement.getElementsByTagName("epanetui_plugin")

    class InitStruct:
        download_url = []
        plugins = []
        description = []
        about = []
        version = []
        homepage = []
        author_name = []
        uploaded_by = []
        tracker = []
        repository = []
        tags = []

    xml_values = InitStruct()

    for i, plugin in enumerate(getPlugins):
        xml_values.download_url.append(plugin.getElementsByTagName("download_url")[0].firstChild.data)
        xml_values.plugins.append(plugin.getElementsByTagName("file_name")[0].firstChild.data[0:-4])
        xml_values.description.append(plugin.getElementsByTagName("description")[0].firstChild.data)
        xml_values.about.append(plugin.getElementsByTagName("about")[0].firstChild.data)
        xml_values.version.append(plugin.getElementsByTagName("version")[0].firstChild.data)
        xml_values.homepage.append(plugin.getElementsByTagName("homepage")[0].firstChild.data)
        xml_values.author_name.append(plugin.getElementsByTagName("author_name")[0].firstChild.data)
        xml_values.uploaded_by.append(plugin.getElementsByTagName("uploaded_by")[0].firstChild.data)
        xml_values.tracker.append(plugin.getElementsByTagName("tracker")[0].firstChild.data)
        xml_values.repository.append(plugin.getElementsByTagName("repository")[0].firstChild.data)
        xml_values.tags.append(plugin.getElementsByTagName("tags")[0].firstChild.data)

    del getPlugins, doc, data

    # Check if plugin
    if choice is None:
        choice = 99
    if choice == 1:
        global self, xml_values
        self = pluginManagerUI()
        self.setWindowTitle('Manage and Install Plugins...')

        for plugin in xml_values.plugins:
            item = QtGui.QListWidgetItem()
            item.setText(plugin)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.listWidget.addItem(item)

        self.install_re.clicked.connect(btn_installed)
        self.uninstall.clicked.connect(btn_uninstalled)
        self.listWidget.clicked.connect(update_metadata)
        self.listWidget.itemSelectionChanged.connect(update_metadata)

        self.listWidget.setCurrentRow(0)
        self.show()

        self.update_metadata()

        b # error to show ui

def update_metadata():
    global xml_values, self

    curr = self.listWidget.currentIndex()
    current_index = curr.row()
    plugin_name_sel = str(xml_values.plugins[current_index])
    version = str(xml_values.version[current_index])
    desc = str(xml_values.description[current_index])
    about = str(xml_values.about[current_index])
    homepage = str(xml_values.homepage[current_index])
    download = str(xml_values.download_url[current_index])
    tracker = str(xml_values.tracker[current_index])
    repo = str(xml_values.repository[current_index])
    tags = str(xml_values.tags[current_index])
    author = str(xml_values.author_name[current_index])
    uploadedby = str(xml_values.uploaded_by[current_index])

    self.textEdit.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Plugin Name:</span><span style=\" font-family:\'Courier New\'; font-size:8pt; color:#000000; background-color:#ffffff;\">"+ plugin_name_sel +" </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Version    :</span><span style=\" font-family:\'Courier New\'; font-size:8pt; color:#000000; background-color:#ffffff;\">" + version +"</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Description:</span><span style=\" font-family:\'Courier New\'; font-size:8pt; color:#000000; background-color:#ffffff;\">" + desc +"</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">About      :</span><span style=\" font-family:\'Courier New\'; font-size:8pt; color:#000000; background-color:#ffffff;\">" + about +"</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Homepage   :</span><span style=\" font-family:\'Courier New\'; font-size:8pt; color:#000000; background-color:#ffffff;\"> </span><span style=\" font-size:8pt; color:#0000ff;\">" + homepage +"</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Author     :</span><span style=\" font-family:\'Courier New\'; font-size:8pt; color:#000000; background-color:#ffffff;\">"+ author +"</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Download   : </span><span style=\" font-size:8pt; color:#0000ff;\">" + download +"</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Uploaded by: </span><span style=\" font-family:\'Courier New\'; font-size:8pt; color:#000000; background-color:#ffffff;\">"+uploadedby+"</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Tracker    : </span><span style=\" font-size:8pt; color:#0000ff;\">" + tracker +"</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Repository : </span><span style=\" font-size:8pt; color:#0000ff;\">" + repo +"</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Tags       : </span><span style=\" font-family:\'Courier New\'; font-size:8pt; color:#000000; background-color:#ffffff;\">" + tags +"</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New\'; font-size:8pt; font-weight:600; color:#000000;\"><br /></p></body></html>")

def save_session(session):
    global session_new
    session_new = session

def btn_installed():
    global self, xml_values, session_new

    curr = self.listWidget.currentIndex()
    current_index = curr.row()
    #url = xml_values.download_url[current_index]
    plugin_name_sel = xml_values.plugins[current_index]
    url = 'https://raw.githubusercontent.com/KIOS-Research/EPANET-Plugins/dev/'+plugin_name_sel+'.zip'

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

    refresh_menuPlugin(session_new)
    save_session(session_new)

    QMessageBox.information(None, plugin_name_sel, 'Plugin installed successfully.', QMessageBox.Ok)

def refresh_menuPlugin(session):

    # Clear all plugins
    session.menuPlugins.clear()

    session.plugins = session.get_plugins()

    session.populate_plugins_menu()

def btn_uninstalled():
    global self, xml_values, session_new

    curr = self.listWidget.currentIndex()
    current_index = curr.row()
    plugin_name = xml_values.plugins[current_index]

    reply = QMessageBox.question(None, 'EPANET Python Plugin Installer',
                                 'Are you sure you want to uninstall the following plugin?\n'+'('+plugin_name+')',
                                 QMessageBox.Yes | QMessageBox.No)


    if reply == QMessageBox.Yes:

        # Clear all plugins
        session_new.menuPlugins.clear()
        #session_new.plugins = session_new.get_plugins()

        for plugin in session_new.plugins:
            if plugin_name in plugin['name']:
                session_new.plugins.remove(plugin)
                #break

        # session.plugins = session.get_plugins()
        shutil.rmtree(os.getcwd() + '\\plugins\\' + plugin_name)

        session_new.populate_plugins_menu()
        save_session(session_new)

        QMessageBox.information(None, plugin_name,'Plugin uninstalled successfully.', QMessageBox.Ok)