import mongoengine as me
from Person import Person
import xml.etree.ElementTree as ET


class Crowd(me.Document):
    persons = me.ListField(me.ReferenceField(Person))

    def to_xml(self):
        root = ET.Element('CROWD')
        for pers in self.persons:
            root.append(pers.to_xml())
        return root