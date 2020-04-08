#!/usr/bin/python3
'''Fabric script that generates a .tgz archive from the contents
   of Airbnb_clone_v2
'''
from datetime import datetime
from fabric.api import local


def do_pack():
    """function"""
    local("mkdir -p versions")
    full = "versions/web_static_{}.tgz.format(
        datetime.now.strftime("%Y%m%d%H%M%S"))
    return(local("tar -cvzf {} web_static".format(full)))
