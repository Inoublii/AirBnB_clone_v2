#!/usr/bin/python3
'''Fabric script
'''
from time import strftime
from fabric.api import *


def do_pack():
    """function"""

    datenow = strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    creat = local("tar -cvzf versions/web_static_{}.tgz web_static".format(datenw))
    if creat.succeeded:
        return ("versions/web_static_{}".format(datenow))
    else:
        return None
