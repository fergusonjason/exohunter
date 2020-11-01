from lxml import etree
from io import BytesIO

# xml_source should be a Byte literal
def parse_vizier(xml_source):

    bytes_xml = BytesIO(xml_source)
    tree = etree.parse(bytes_xml)

    # get all fields
    table_fields = tree.xpath("/VOTABLE/TABLE/FIELD")
    for field in table_fields:
        name = field
        pass

    # build a name array

    # build a type dict
    # get the xml
    parsed_xml = etree.xml(xml_source)
    pass