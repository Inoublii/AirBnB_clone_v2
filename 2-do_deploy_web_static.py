#!/usr/bin/python3
'''Fabric script that generates a .tgz archive from the contents
   of Airbnb_clone_v2
'''
from datetime import datetime
from fabric.api import local
import sys
import os

def do_pack():
    """function"""
    local("mkdir -p versions")
    full = "versions/web_static_{}.tgz".format(
        datetime.now.strftime("%Y%m%d%H%M%S"))
    if full is None:
        return(None)
    return(local("tar -cvzf {} web_static".format(full)))
def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return(False)
    deploy_file = archive_path.split('/')[1].split('.')[0]
    path_archve = "/data/web_static/releases/"
    put(archive_path, "/tmp/")
    
    
