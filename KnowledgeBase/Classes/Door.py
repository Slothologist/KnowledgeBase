import mongoengine as me
from Room import Room
from Annotation import Annotation
import xml.etree.ElementTree as ET


class Door(me.Document):
    roomOne = me.ReferenceField(Room)
    roomTwo = me.ReferenceField(Room)
    annotation = me.EmbeddedDocumentField(Annotation)

    def to_xml(self):
        attribs = {x: self.__getattribute__(x) for x in self._fields}
        annot = attribs.pop('annotation')
        attribs.pop('id')
        root = ET.Element('DOOR', attrib={'roomOne':attribs['roomOne'].name, 'roomTwo':attribs['roomTwo'].name})
        root.append(annot.to_xml())
        gen = ET.SubElement(root, 'GENERATOR')
        gen.text = 'unknown'
        return root