#!/usr/bin/python3
""" Fabric script  that distributes an archive to the web servers,
using the function do_deploy """

from datetime import datetime
from fabric.api import *
import os


def do_pack():
    """ function that returns an archive path """
    try:
        if not os.path.exist("versions"):
            local("mkdir versions")
        date = datetime.now()
        date = date.strftime("%Y%m%d%H%M%S")
        new_versions = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(new_versions))
        return new_versions
    except:
        return None
