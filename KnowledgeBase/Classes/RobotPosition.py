import mongoengine as me
import xml.etree.ElementTree as ET


class RobotPosition(me.EmbeddedDocument):
    label = me.StringField(max_length=100, default='')
    x = me.FloatField(default=0.0)
    y = me.FloatField(default=0.0)
    theta = me.FloatField(default=0.0)

    def to_xml(self):
        root = ET.Element('VIEWPOINT', attrib={'label': self.label, 'category': 'VIEW'})
        attribs = vars(self)
        attribs.pop('label')
        attribs['kind'] = 'absolute'
        vp = ET.SubElement(root, 'ROBOTPOSITION', attrib=attribs)
        gen = ET.SubElement(vp, 'GENERATOR')
        gen.text = 'unknown'
        return root
