# Name: Basemaps
# Author: Marios S. Kyriakou, KIOS Research and Innovation Center of Excellence (KIOS CoE)
# Email: mariosmsk@gmail.com
# License: MIT

# This plugin works with EPANET MTP5r1:
# https://github.com/USEPA/SWMM-EPANET_User_Interface/releases/tag/MTP5r1
import os

plugin_name = "Basemaps"
plugin_create_menu = True
__all__ = {"Google Satellite":1, "Openstreetmap":2}


def checkBasemaps(session, mapname):
    status = True
    for tlayer in session.map_widget.base_group.findLayers():
        if tlayer.layer().name() == mapname:
            session.map_widget.base_group.removeLayer(tlayer.layer())
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

    elif choice == 2:
        mapname = "Openstreetmap.xml"
        status = checkBasemaps(session, mapname)
        if not status:
            return

    if choice ==1 or choice == 2:
        urlWithParams = path + mapname
        session.map_widget.addRasterLayer(urlWithParams)
        session.map_widget.refresh_extent_needed = False
