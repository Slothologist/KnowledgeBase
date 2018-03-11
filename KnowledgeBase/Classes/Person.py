import mongoengine as me
from Positiondata import Positiondata
import xml.etree.ElementTree as ET


class Person(me.Document):
    ageFrom = me.IntField(default=0)
    ageTo = me.IntField(default=0)
    gender = me.StringField(max_length=50, default='')
    shirtcolor = me.StringField(max_length=50, default='')
    pose = me.StringField(max_length=50, default='')
    gesture = me.StringField(max_length=50, default='')
    lastKnownPosition = me.EmbeddedDocumentField(Positiondata)
    name = me.StringField(max_length=100, default='')
    uuid = me.StringField(max_length=50, required=True, primary_key=True)
    faceId = me.IntField(default=-1)
    # pointcloud

    def to_xml(self):
        attribs = {x: self.__getattribute__(x) for x in self._fields}
        posi = attribs.pop('lastKnownPosition')
        attribs = {x: str(attribs[x]) for x in attribs}

        root = ET.Element('PERSON', attrib=attribs)
        root.append(posi.to_xml())
        return root


    @classmethod
    def from_xml(cls):
        pass