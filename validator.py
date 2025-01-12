# -*- coding: utf-8 -*-

""" E-ING GML validator

    Check XML/GML documents using XSD schema.

    usage validator.py xml_file
"""
import sys
from sys import argv, exit
from lxml import etree
import codecs
import configparser
import os.path

APPNAME = "eing_gml_validator"
KEY_XSD = "xsd"
inifile = os.path.normpath(os.path.join(os.getcwd(), APPNAME+".ini"))

def get_xsd_filename():
    xsd = ""
    if os.path.isfile(inifile):
        config = configparser.ConfigParser()
        config.read_file(codecs.open(inifile, "r", "utf-8"))
        if KEY_XSD in config[APPNAME]:
            xsd = config[APPNAME][KEY_XSD]
    return xsd


def validate_gml(xsd_filename, gml_filename):

    logfilaname = gml_filename + ".txt"
    logfile = open(logfilaname, "w", encoding="utf-8")

    try:
        xmlschema_doc = etree.parse(xsd_filename)
    except OSError:
        logfile.write(f"{xsd_filename} missing schema file\n")
        exit(2)
    try:
        xmlschema = etree.XMLSchema(xmlschema_doc)
    except etree.XMLSchemaParseError as e:
        logfile.write(f"{xsd_filename} syntax error in schema\n")
        logfile.write(e)
        logfile.close()
        exit(3)

    etree.clear_error_log()

    try:
        doc = etree.parse(gml_filename)
    except (OSError, etree.XMLSyntaxError):
        logfile.write(f"{gml_filename} invalid or missing XML/GML file\n")
        logfile.close()
        exit(4)

    valid = xmlschema.validate(doc)
    if not valid:
        logfile.write(str(xmlschema.error_log.last_error))
    else:
        logfile.write(f"{gml_filename} is VALID\n")
    logfile.close()

    if os.path.isfile(logfilaname):
        os.startfile(logfilaname, 'open')

def main():
    args = sys.argv
    gmlfn = ""
    if len(args) >= 2:
        gmlfn = args[1]
        xsdfn = get_xsd_filename()
        validate_gml(xsdfn, gmlfn)
    else:
        os.startfile(inifile, 'open')

if __name__ == '__main__':
    main()