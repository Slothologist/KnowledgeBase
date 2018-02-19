import mongoengine as me
from Location import Location
import xml.etree.ElementTree as ET


class RCObject(me.Document):
    name = me.StringField(max_length=50, unique=True, default='')
    location = me.ReferenceField(Location)
    category = me.StringField(max_length=50, default='')
    shape = me.StringField(max_length=50, default='')
    color = me.StringField(max_length=50, default='')
    type = me.StringField(max_length=50, default='')
    size = me.IntField(default=0)
    weight = me.IntField(default=0)

    def to_xml(self):
        attribs = vars(self)
        location = attribs.pop('location')
        attribs['location'] = location.name
        attribs['room'] = location.room.name
        attribs['graspdifficulty'] = '0'
        root = ET.Element('ROOM', attrib=attribs)
        gen = ET.SubElement(root, 'GENERATOR')
        gen.text = 'unknown'
        return root
