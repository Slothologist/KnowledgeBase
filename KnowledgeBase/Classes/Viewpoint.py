import mongoengine as me
import xml.etree.ElementTree as ET
from Positiondata import Positiondata


class Viewpoint(me.EmbeddedDocument):
    label = me.StringField(max_length=100, default='')
    positiondata = me.EmbeddedDocumentField(Positiondata)

    def to_xml(self):
        attribs = {x: self.__getattribute__(x) for x in self._fields}
        posi = attribs.pop('positiondata')
        root = ET.Element('VIEWPOINT', attrib=attribs)
        root.append(posi.to_xml())
        return root


    @classmethod
    def from_xml(cls, xml_tree):
        vp = Viewpoint()
        vp.label = xml_tree.get('label')
        for potential_posi in xml_tree.getchildren():
            if potential_posi.tag == Positiondata.get_tag():
                vp.positiondata = Positiondata.from_xml(potential_posi)
        return vp
