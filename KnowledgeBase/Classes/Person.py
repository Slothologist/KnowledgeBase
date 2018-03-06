import mongoengine as me
from RobotPosition import Robotposition
import xml.etree.ElementTree as ET


class Person(me.Document):
    ageFrom = me.IntField(default=0)
    ageTo = me.IntField(default=0)
    gender = me.StringField(max_length=50, default='')
    shirtcolor = me.StringField(max_length=50, default='')
    pose = me.StringField(max_length=50, default='')
    gesture = me.StringField(max_length=50, default='')
    lastKnownPosition = me.EmbeddedDocumentField(Robotposition)
    name = me.StringField(max_length=100, default='')
    uuid = me.StringField(max_length=50, required=True, primary_key=True)
    faceId = me.IntField(default=-1)
    # pointcloud

    def to_xml(self):
        attribs = {x: self.__getattribute__(x) for x in self._fields}
        posi = attribs.pop('lastKnownPosition')
        attribs = {x: str(attribs[x]) for x in attribs}

        root = ET.Element('PERSON', attrib=attribs)
        gen = ET.SubElement(root, 'GENERATOR')
        gen.text = 'unknown'
        point = ET.SubElement(root, 'POINT2D', attrib={'scope': 'GLOBAL', 'x': str(posi.x), 'y': str(posi.y)})
        pointgen = ET.SubElement(point, 'GENERATOR')
        pointgen.text = 'unknown'
        return root