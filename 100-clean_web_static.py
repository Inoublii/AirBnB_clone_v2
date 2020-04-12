#!/usr/bin/python3
'''Fabric script that generates a .tgz archive from the contents
   of Airbnb_clone_v2
'''
from time import strftime
from fabric.api import *
from fabric.operations import run, put, sudo
import os.path
from datetime import datetime
env.hosts = ["35.227.78.112	", "54.81.167.121"]


def do_pack():
    ''' def do pack
    '''
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    path = 'versions/web_static_' + date + '.tgz'
    if not (os.path.exists("versions")):
        local('mkdir -p versions')
    local('tar -cvzf ' + path + ' web_static')
    if (os.path.exists(path)):
        return path
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


def do_clean(number=0):
    """
    deletes out-of-date archives.
    Return True if there is not operation to do otherwise False if an error is
    raised
    """
    try:
        number = int(number)
    except Exception:
        return False
    archives_nb = local('ls -ltr versions | wc -l', capture=True).stdout
    archives_nb = int(archives_nb) - 1
    if (archives_nb <= 0 or archives_nb == 1):
        return True
    if (number == 0 or number == 1):
        remove_nb = archives_nb - 1
    else:
        remove_nb = archives_nb - number
        if (remove_nb <= 0):
            return True
    archives_list = local("ls -ltr versions | tail -n " + str(archives_nb) + "\
            | head -n \
            " + str(remove_nb) + "\
            | awk '{print $9}'", capture=True).rsplit("\n")
    if len(archives_list) >= 1:
        for archive_name in archives_list:
            if (archive_name != ''):
                local('rm versions/' + archive_name)
                run('rm -rf /data/web_static/releases/\
                    ' + archive_name.split('.')[0])
