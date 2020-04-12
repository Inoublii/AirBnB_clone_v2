#!/usr/bin/python3
'''Fabric script that generates a .tgz archive from the contents
   of Airbnb_clone_v2
'''
from time import strftime
from fabric.api import *
import os
from datetime import datetime
import sys
env.user = 'ubuntu'
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
    '''func deploy'''
    if not archive_path:
        return(False)
    try:
        put(archive_path, "/tmp/")
        deploy_file = archive_path.split("/")[1].split(".")[0]
        file_path = file_deploy.split(".")[0]
        path = archive_path.split("/")[-1]
        deploy_path = "/data/web_static/releases/{}".format(deploy_file)
        run("mkdir -p {}".format(deploy_path))
        run("tar -xzf /tmp/{} - C {}".format(path, deploy_path))
        run("rm -rf /tmp/{}".format(path))
        run("mv {}/web_static/* {}/".format(deploy_path, deploy_path))
        run("rm -rf {}/web_static".format(deploy_path))
        run("rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(deploy_path))
        return(True)
    except BaseException:
        return(False)
