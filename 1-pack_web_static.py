#!/usr/bin/python3
""" script that generates a .tgz archive
"""

from datetime import datetime
from fabric.api import run, cd, local


def do_pack():
    """func that create a dir and a file """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    path = "versions/web_static_{}.tgz" .format(time)
    var = local("tar -czvf {} web_static/" .format(path))
    if var == 0:
        return path
    else:
        return None
