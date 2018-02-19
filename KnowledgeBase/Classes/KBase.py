import mongoengine as me
from Context import Context
from Crowd import Crowd
from RCObjects import RCObjects
from Arena import Arena
import xml.etree.ElementTree as ET


class KBase(me.Document):
    identifier = me.StringField(max_length=50, unique=True)
    context = me.ReferenceField(Context)
    crowd = me.ReferenceField(Crowd)
    rcobjects = me.ReferenceField(RCObjects)
    arena = me.ReferenceField(Arena)

    def to_xml(self):
        root = ET.Element('KBASE')
        gen = ET.SubElement(root, 'GENERATOR')
        gen.text = 'unknown'
        root.append(self.crowd.to_xml())
        root.append(self.arena.to_xml())
        root.append(self.rcobjects.to_xml())
        root.append(self.context.to_xml())
        return root