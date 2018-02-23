import mongoengine as me
from RCObject import Rcobject
import xml.etree.ElementTree as ET


class Rcobjects(me.Document):
    rcobjects = me.ListField(me.ReferenceField(Rcobject))

    def to_xml(self):
        root = ET.Element('RCOBJECTS')
        gen = ET.SubElement(root, 'GENERATOR')
        gen.text = 'unknown'
        for ob in self.rcobjects:
            root.append(ob.to_xml())
        return root