import mongoengine as me
from RobotPosition import RobotPosition
import xml.etree.ElementTree as ET


class Annotation(me.EmbeddedDocument):
    label = me.StringField(max_length=100, default='')
    polygon = me.PolygonField()
    viewpoints = me.ListField(me.EmbeddedDocumentField(RobotPosition))

    def to_xml(self):
        attribs = vars(self)
        viewpoints = attribs.pop('viewpoints')
        polygon = attribs.pop('polygon')
        root = ET.Element('ANNOTATION', attrib=attribs)
        gen = ET.SubElement(root, 'GENERATOR')
        gen.text = 'unknown'
        for point in viewpoints:
            root.append(point.to_xml())
        #todo polygon
        return root