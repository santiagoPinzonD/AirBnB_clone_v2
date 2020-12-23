#!/usr/bin/python3
""" script that generates a .tgz archive
"""


import os
from fabric.api import *
from datetime import datetime


def do_pack():
    """func that create a dir and a file """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    path = "versions/web_static_{}.tgz" .format(time)
    var = local("tar -czvf {} web_static/" .format(path))
    if var.succeeded:
        return path
    else:
        return None


def do_deploy(archive_path):
    """create function of deploy"""
    if os.path.exists(archive_path) is False:
        return False
    try:
        pathfix = archive_path.split("/")[-1]
        whithouttgz = pathfix.split(".")[0]
        path = "/data/web_static/releases"
        put("{}".format(archive_path), "/tmp/{}".format(pathfix))
        run("sudo mkdir -p {}/{}/" .format(path, whithouttgz))
        run("sudo tar -xzf /tmp/{} -C {}/{}/" .format(pathfix,
                                                      path, whithouttgz))
        run("sudo rm /tmp/{}".format(pathfix))
        run("sudo mv {}/{}/web_static/* {}/{}/".format(path,
                                                       whithouttgz,
                                                       path, whithouttgz))
        run("sudo rm -rf {}/{}/web_static" .format(path, whithouttgz))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf {}/{}/ /data/web_static/current" .format(path,
                                                                  whithouttgz))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """distributes an archive to your web servers"""
    path = do_pack()
    if path is None:
        return False
    else:
        return do_deploy(path)
