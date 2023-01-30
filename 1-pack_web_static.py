#!/usr/bin/python3

''' That generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.'''


import os.path
from fabric.api import local
from datetime import datetime


def do_pack():
    ''' Archive a bunch of files to versions with fabrics '''

    dt = datetime.utcnow()
    file = 'versions/web_static_{}{}{}{}{}{}.tgz'
    file = file.format(
            dt.year,
            dt.month,
            dt.day,
            dt.hour,
            dt.minute,
            dt.second)
    if os.path.isdir('versions') is False:
        if local('mkdir -p versions').failed is True:
            return None
    if local(('tar -cvzf {} web_static').format(file)).failed is True:
        return None
    return file
