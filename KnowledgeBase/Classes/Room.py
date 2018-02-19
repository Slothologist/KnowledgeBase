import mongoengine as me
from Annotation import Annotation
import xml.etree.ElementTree as ET


class Room(me.Document):
    name = me.StringField(max_length=50, unique=True, default='')
    numberOfDoors = me.IntField(default=0)
    annotation = me.EmbeddedDocumentField(Annotation)

    def to_xml(self):
        attribs = vars(self)
        annot = attribs.pop('annotation')
        root = ET.Element('ROOM', attrib=attribs)
        root.append(annot.to_xml())
        gen = ET.SubElement(root, 'GENERATOR')
        gen.text = 'unknown'
        return root