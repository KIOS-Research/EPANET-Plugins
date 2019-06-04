# Name: Basemaps
# Author: Marios S. Kyriakou, KIOS Research and Innovation Center of Excellence (KIOS CoE)
# Email: mariosmsk@gmail.com
# License: MIT

# This plugin works with EPANET MTP4r2:
# https://github.com/USEPA/SWMM-EPANET_User_Interface/releases/tag/MTP4r2
import os

plugin_name = "Basemaps"
plugin_create_menu = True
__all__ = {"Google Satellite":1, "Openstreetmap":2}


def checkBasemaps(session, mapname):
    status = True
    for tlayer in session.map_widget.base_group.findLayers():
        if tlayer.layer().name() == mapname:
            session.map_widget.remove_layers([tlayer.layer()])
            session.map_widget.base_group.removeChildNode(tlayer)
            status = False
            break
    return status

def run(session=None, choice=None):

    path = os.getcwd() + "\\plugins\\Basemaps\\"
    if choice is None:
        choice = 99
    if choice == 1:
        mapname = "Google Satellite.xml"
        status = checkBasemaps(session, mapname)
        if not status:
            return

        urlWithParams = path + mapname
        session.map_widget.addRasterLayer(urlWithParams)
        path_only, file_only = os.path.split(filename)
        if path_only != directory:
            session.program_settings.setValue("GISDataDir", path_only)
            session.program_settings.sync()
        session.map_widget.refresh_extent_needed = False

    elif choice == 2:
        mapname = "Openstreetmap.xml"
        status = checkBasemaps(session, mapname)
        if not status:
            return

        urlWithParams = path + mapname
        session.map_widget.addRasterLayer(urlWithParams)
        path_only, file_only = os.path.split(filename)
        if path_only != directory:
            session.program_settings.setValue("GISDataDir", path_only)
            session.program_settings.sync()
        session.map_widget.refresh_extent_needed = False
