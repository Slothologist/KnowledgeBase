import mongoengine as me
import xml.etree.ElementTree as ET


class Robotposition(me.EmbeddedDocument):
    label = me.StringField(max_length=100, default='')
    x = me.FloatField(default=0.0)
    y = me.FloatField(default=0.0)
    theta = me.FloatField(default=0.0)

    def to_xml(self):
        attribs = {x: self.__getattribute__(x) for x in self._fields}
        label = attribs.pop('label')
        attribs['kind'] = 'absolute'
        attribs = {x: str(attribs[x]) for x in attribs}
        root = ET.Element('VIEWPOINT', attrib={'label': label, 'category': 'VIEW'})
        vp = ET.SubElement(root, 'ROBOTPOSITION', attrib=attribs)
        gen = ET.SubElement(vp, 'GENERATOR')
        gen.text = 'unknown'
        return root

    @classmethod
    def from_xml(cls, xml_tree):
        roboposi = Robotposition()
        roboposi.label = xml_tree.get('label')
        roboposi_found = False
        for child in xml_tree.getchildren():
            if child.tag == 'ROBOTPOSITION':
                roboposi_found = True
                for potentional_posi in child.getchildren():
                    if potentional_posi.tag == 'POSITION':
                        roboposi.x = float(potentional_posi.get('x'))
                        roboposi.y = float(potentional_posi.get('y'))
                        roboposi.theta = float(potentional_posi.get('theta'))
        if not roboposi_found:
            print('Could not find robotposition in viewpoint ' + str(roboposi.label))


        return roboposi

