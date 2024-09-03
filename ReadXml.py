from Constants import PERCEPCIONES, DEDUCCIONES
import xml.etree.ElementTree as ET
import logging
logger = logging.getLogger(__name__)

__head__ = '{http://www.sat.gob.mx/nomina12}'

def GetXmlFromFile(path):
    file = open(path, 'r')
    sXml = file.read()
    file.close()

    root = ET.fromstring(sXml)
    
    return root

def GetXmlIdentifier(xml):
    return [xml.attrib.get('Fecha')]

# Percepciones
def GetConceptsFromPercepcion(xml):
    return [percepcion.attrib.get('Concepto') for percepcion in xml.iter(f'{__head__}Percepcion')]

def GetValuesFromPercepcion(xml):
    percepciones = []
    for percepcion in xml.iter(f'{__head__}Percepcion'):
        concepto = percepcion.attrib.get('Concepto')
        if(concepto in PERCEPCIONES):
            percepciones.append([f'{concepto}_gravado', percepcion.attrib.get('ImporteGravado')])
            percepciones.append([f'{concepto}_exento', percepcion.attrib.get('ImporteExento')])
        else:
            percepciones.append([concepto, ''])

    return percepciones

# Deducciones
def GetConceptsFromDeduccion(xml):
    return [percepcion.attrib.get('Concepto') for percepcion in xml.iter(f'{__head__}Deduccion')]

def GetValuesFromDeduccion(xml):
    deducciones = []
    for deduccion in xml.iter(f'{__head__}Deduccion'):
        concepto = deduccion.attrib.get('Concepto')
        if(concepto in DEDUCCIONES):
            deducciones.append([concepto, deduccion.attrib.get('Importe')])

    return deducciones

def GetHeaders():
    headers = ['FECHA']
    for colName in PERCEPCIONES:
        headers.append(f'{colName}_gravado')
        headers.append(f'{colName}_exento')
    for colName in DEDUCCIONES:
        headers.append(f'{colName}')

    return headers

def FormatColumn(headers, itentifiers, percepciones, deducciones):
    row = [itentifiers[0]]
    for colName in headers:
        if colName == 'FECHA':
            continue
        
        columnFilter = [col for col in percepciones if col[0] == colName]
        if(columnFilter == []):
            columnFilter = [col for col in deducciones if col[0] == colName]
        if(columnFilter == []):
            columnFilter = [[colName, '0.00']]
            
        column = columnFilter[0]
        value = column[1]

        row.append(value)

    return row