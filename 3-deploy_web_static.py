#!/usr/bin/python3
""" Fabric script that creates and distributes an archive to your web servers,
using the function deploy """


from datetime import datetime
from fabric.api import *
import os
from shlex import split

env.host = ['35.231.181.131', '35.227.25.5']
env.user = "ubuntu"


def do_pack():
    """ function that returns an archive path """
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")
        date = datetime.now()
        date = date.strftime("%Y%m%d%H%M%S")
        new_versions = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(new_versions))
        return new_versions
    except:
        return None


def do_deploy(archive_path):
    """  distributes an archive to your web servers """
    if not os.path.exists(archive_path):
        return False
    try:
        path = "/data/web_static/releases/"
        file_name = os.path.basename(archive_path)
        put(file_name, '/tmp/{}'.format(file_name))
        spaces = file_name.replace('.', ' ')
        without_ext = spaces.split(' ')
        ext_out = with_ext[-2]

        run('mkdir -p /data/web_static/releases/{}'.format(ext_out))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, ext_out))
        run('rm /tmp/{}'.format(file_name))
        run('mv {}{}/web_static/* {}{}/'.format(path, ext_out, path, ext_out))
        run('rm -rf {}{}/web_static'.format(path, without_ext1))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, ext_out))
        return True
    except:
        return False


def deploy():
    """ deploy """
    path = do_pack()
    if not path:
        return False

    new_path = do_deploy(path)
    return (new_path)
