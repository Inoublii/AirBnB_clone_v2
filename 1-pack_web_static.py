#!/usr/bin/python3
'''Fabric script
'''
from datetime import datetime
from fabric.api import *


def do_pack():
    """function"""

    local("mkdir -p versions")
    creat = local("tar -cvzf versions/web_static_{}.tgz web_static".format(strftime("%Y%m%d%H%M%S")))
    if creat.succeeded:
        return ("versions/web_static_{}".format(strftime("%Y%m%d%H%M%S")))
    else:
        return None
