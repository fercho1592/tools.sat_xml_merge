import sys
from ReadXml import GetXmlFromFile, GetValuesFromPercepcion, GetValuesFromDeduccion, GetXmlIdentifier, GetHeaders, FormatColumn
from Common import unique, GetFilesPathInDir
from WriteCsv import CreateFileWriter, WriteLine, CloseFile
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

# Main process
if __name__ == '__main__':
    dir = sys.argv[1]

    invoiceRows = []
    logger.info(f'Create file in {dir}')
    [file, csvWriter] = CreateFileWriter(dir)

    try:
        logger.info(f'Getting XML files form {dir}')
        filesPath = GetFilesPathInDir(dir)
        headers = GetHeaders()
        WriteLine(csvWriter, headers)

        for filePath in filesPath:
            logger.info(f'Open {filePath}')
            xml = GetXmlFromFile(filePath)
            
            identifiers = GetXmlIdentifier(xml)
            logger.debug(identifiers)
            perceptions = GetValuesFromPercepcion(xml)
            logger.debug(perceptions)
            deductions = GetValuesFromDeduccion(xml)
            logger.debug(deductions)

            logger.info('Formatting row')
            row = FormatColumn(headers, identifiers, perceptions, deductions)

            logger.info('Writing row in file')
            WriteLine(csvWriter, row)

        logger.info('Finished succesfully')
    except Exception as err:
        logger.error('Finished with errors')
        logger.error(err)
    finally:
       CloseFile(file, csvWriter)
