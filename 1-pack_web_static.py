#!/usr/bin/python3
'''Fabric script
'''
from datetime import datetime
from fabric.api import local


def do_pack():
    """function"""
    n = datetime.now()
    name = "web_static_{}{}{}{}{}{}.tgz".format(n.year, n.month,
                                                n.day, n.hour,
                                                n.minute, n.second)
    local("mkdir -p versions")
    if name is None:
        return(None)
    return(local("tar -cvzf {} web_static".format(name)))
