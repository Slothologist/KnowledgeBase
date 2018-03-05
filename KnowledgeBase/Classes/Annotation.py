import mongoengine as me
from RobotPosition import Robotposition
import xml.etree.ElementTree as ET

point_shrinking_factor = 1000


def serialize_point2d(point):
    attribs = {'x': str(point[0] * point_shrinking_factor), 'y': str(point[1] * point_shrinking_factor), 'scope': 'GLOBAL'}
    root = ET.Element('POINT2D', attrib=attribs)
    gen = ET.SubElement(root, 'GENERATOR')
    gen.text = 'unknown'
    return root


class Annotation(me.EmbeddedDocument):
    label = me.StringField(max_length=100, default='')
    polygon = me.PolygonField()
    viewpoints = me.ListField(me.EmbeddedDocumentField(Robotposition))

    def to_xml(self):
        attribs = {x: self.__getattribute__(x) for x in self._fields}
        viewpoints = attribs.pop('viewpoints')
        polygon = attribs.pop('polygon')
        attribs = {x: str(attribs[x]) for x in attribs}
        root = ET.Element('ANNOTATION', attrib=attribs)
        gen = ET.SubElement(root, 'GENERATOR')
        gen.text = 'unknown'
        for point in viewpoints:
            root.append(point.to_xml())
        if polygon:  # check if polygon was set (may not be for )
            poly = ET.SubElement(root, 'PRECISEPOLYGON')
            polygen = ET.SubElement(poly, 'GENERATOR')
            polygen.text = 'unknown'
            if type(polygon) == dict:  # the polygon was loaded from database
                for point in polygon['coordinates'][0][:-1]: #omit last point wich is also the first one (geojson specific stuff)
                    poly.append(serialize_point2d(point))
            elif type(polygon) == list:  # the polygon was created "manually"
                for point in polygon[0][:-1]: #omit last point wich is also the first one (geojson specific stuff)
                    poly.append(serialize_point2d(point))
        else:
            print('Warning: Annotation with label \"' + attribs['label'] + '\" has no PrecisePolygon')
        return root