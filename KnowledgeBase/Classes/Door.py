import mongoengine as me
from Room import Room
from Annotation import Annotation
import xml.etree.ElementTree as ET


class Door(me.Document):
    roomOne = me.ReferenceField(Room)
    roomTwo = me.ReferenceField(Room)
    annotation = me.EmbeddedDocumentField(Annotation)

    def to_xml(self):
        attribs = vars(self)
        annot = attribs.pop('annotation')
        root = ET.Element('DOOR', attrib={'roomOne':self.roomOne.name, 'roomTwo':self.roomTwo.name})
        root.append(annot.to_xml())
        gen = ET.SubElement(root, 'GENERATOR')
        gen.text = 'unknown'
        return root