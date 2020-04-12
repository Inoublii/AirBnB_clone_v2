#!/usr/bin/python3
'''Fabric script
'''
from time import strftime
from fabric.api import *
import os


def do_pack():
    """fabric script that
    compresses files"""

    datenow = strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    creat = local("tar -cvzf versions/web_static_{}.tgz web_static".format(datenow))
    size = os.stat("versions/web_static_{}.tgz".format(datenow)).st_size
    if creat.succeeded:
        print("web_static packed: versions/web_static_{}.tgz -> {}Bytes".format(datenow, size))
    else:
        return None
