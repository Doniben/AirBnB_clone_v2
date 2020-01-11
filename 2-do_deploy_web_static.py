#!/usr/bin/python3
""" Fabric script that distributes an archive to
your web servers, using the function do_deploy """

import os
from fabric.api import *
from shlex import split

env.host = [
    '35.231.181.131',
    '35.227.25.5'
    ]

env.user = "ubuntu"
# env.use_ssh_config = True
# env.ssh_config_path = '~/.ssh/ssh_config'
# env.key_filename = '~/.ssh/holberton'


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
        print("New version deployed!")
        return True
    except:
        return False
