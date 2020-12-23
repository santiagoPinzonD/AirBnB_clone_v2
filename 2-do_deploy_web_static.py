#!/usr/bin/python3
""" script that generates a .tgz archive
"""

import os
from fabric.api import run, cd, local, env


env.host = ['35.227.48.225', '34.74.219.148']


def do_deploy(archive_path):
    """create function of deploy"""
    pathfix = archive_path.split("/")[-1]
    whithouttgz = pathfix.split(".")
    path = "/data/web_static/releases"
    if os.path.exists(archive_path) is False:
        return False
    try:
        put("{}".format(archive_path), "/tmp/{}".format(pathfix))
        run("sudo mkdir -p {}/{}/" .format(path, whithouttgz[0]))
        run("sudo tar -xzf /tmp/{} -C {}/{}" .format(pathfix,
                                                     path, whithouttgz[0]))
        run("sudo rm /tmp/{}".format(pathfix))
        run("sudo mv {}/{}/web_static/* {}/{}".format(path,
                                                      pathfix, path, pathfix))
        run("sudo rm -rf {}/{}/web_static" .format(path, whithouttgz))
        run("sudo rm -rf /data/web_static/current")
        run("ln -s {}/{}/ /data/web_static/current" .format(path, whithouttgz))
        return True
    except Exception:
        return False
