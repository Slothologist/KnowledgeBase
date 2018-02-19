import mongoengine as me
from RCObjects import RCObjects
from Person import Person
from Room import Room
from Location import Location
from Door import Door
import xml.etree.ElementTree as ET

class Context(me.Document):
    lastquestion = me.StringField(max_length=300, default='But this is the first question!')
    content = me.DynamicField(choices=[RCObjects, Person, Room, Location, Door])

    def to_xml(self):
        attribs = vars(self)
        content = attribs.pop('content')
        root = ET.Element('CONTEXT', attrib=attribs)
        root.append(content.to_xml())
        gen = ET.SubElement(root, 'GENERATOR')
        gen.text = 'unknown'
        return root
