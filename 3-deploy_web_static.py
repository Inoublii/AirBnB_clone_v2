#!/usr/bin/python3
'''Fabric script that generates a .tgz archive from the contents
   of Airbnb_clone_v2
'''
from time import strftime
from fabric.api import *
from fabric.operations import run, put, sudo
import os
import os.path
from datetime import datetime
env.hosts = ["35.227.78.112	", "54.81.167.121"]


def do_pack():
    """fabric script that
    compresses files"""

    datenow = strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    creat = local(
        "tar -cvzf versions/\web_static_{}.tgz web_static".format(datenow))
    size = os.stat("versions/web_static_{}.tgz".format(datenow)).st_size
    if creat.succeeded:
        print("web_static packed:\
versions/web_static_{}.tgz -> {}Bytes".format(datenow, size))
    else:
        return None


def do_deploy(archive_path):
    ''' def deploy '''
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        new_comp = archive_path.split("/")[-1]
        new_folder = ("/data/web_static/releases/" + new_comp.split(".")[0])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(new_folder))
        run("sudo tar -xzf /tmp/{} -C {}".
            format(new_comp, new_folder))
        run("sudo rm /tmp/{}".format(new_comp))
        run("sudo mv {}/web_static/* {}/".format(new_folder, new_folder))
        run("sudo rm -rf {}/web_static".format(new_folder))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {} /data/web_static/current".format(new_folder))
        return True
    except:
        return False


def deploy():
    ''' def deploy '''
    try:
        addr = do_pack()
        take = do_deploy(addr)
        return take
    except:
        return False
