import sys
from os import path, environ, makedirs
from appdirs import *


def getAppData(appname):
    appdata = user_data_dir(appname, appname)
    return appdata


def create_dir_if_not_exists(directory):
    if not path.exists(directory):
        makedirs(directory)


def get_database_path(appname, database):
    appdata = getAppData(appname)
    create_dir_if_not_exists(appdata)
    database_path = path.join(appdata, database)
    return database_path
