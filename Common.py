from os import listdir
from pathlib import Path
from os.path import isfile, join
import logging
logger = logging.getLogger(__name__)

def GetFilesPathInDir(dir):
    fileNamesWithPath = [join(dir, f) for f in listdir(dir) if isfile(join(dir, f)) and '.xml' in f]
    return fileNamesWithPath

def unique(list1):
    unique_list = []
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def Filter(eleList, toFind):
    if (toFind in eleList):
        return True
    else:
        return False

def CreateDirIfNotExist(dir):
    Path(dir).mkdir(parents=True, exist_ok=True)