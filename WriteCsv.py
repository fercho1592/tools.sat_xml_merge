from Common import CreateDirIfNotExist
from os.path import join
from datetime import datetime
import csv
import logging
logger = logging.getLogger(__name__)

def CreateFileWriter(dir):
    now = datetime.now()
    fileName = f'xml_{now.strftime("%Y_%m_%d_%H_%M_%S")}.csv'
    logger.debug(f'Oppening file {fileName}')
    cvsDir = join(dir,'csv')
    CreateDirIfNotExist(cvsDir)
    csvfile = open(join(cvsDir,fileName),'w', newline='')
    fileWriter = csv.writer(csvfile, delimiter=' ', quotechar='_', quoting=csv.QUOTE_MINIMAL)

    return [csvfile, fileWriter]

def WriteLine(fileWriter, column):
    logger.debug(f'Writing column in file: {column}')
    line = ','.join(column)
    logger.debug(line)
    fileWriter.writerow(line)

def CloseFile(file, fileWriter):
    file.close()