import mongoengine as me
from Viewpoint import Viewpoint
from Point2d import Point2d
import xml.etree.ElementTree as ET

class Annotation(me.EmbeddedDocument):
    label = me.StringField(max_length=100, default='')
    polygon = me.PolygonField()
    viewpoints = me.ListField(me.EmbeddedDocumentField(Viewpoint))

    def to_xml(self):
        attribs = {x: self.__getattribute__(x) for x in self._fields}
        viewpoints = attribs.pop('viewpoints')
        polygon = attribs.pop('polygon')
        attribs = {x: str(attribs[x]) for x in attribs}
        root = ET.Element('ANNOTATION', attrib=attribs)
        for point in viewpoints:
            root.append(point.to_xml())
        if polygon:  # check if polygon was set (may not be for )
            poly = ET.SubElement(root, 'PRECISEPOLYGON')
            if type(polygon) == dict:  # the polygon was loaded from database
                for point in polygon['coordinates'][0][:-1]: #omit last point wich is also the first one (geojson specific stuff)
                    poi = Point2d(x=point[0],
                                  y=point[1])
                    poly.append(poi.to_xml())
            elif type(polygon) == list:  # the polygon was created "manually"
                for point in polygon[0][:-1]: #omit last point wich is also the first one (geojson specific stuff)
                    poi = Point2d(x=point[0],
                                  y=point[1])
                    poly.append(poi.to_xml())
        else:
            print('Warning: Annotation with label \"' + attribs['label'] + '\" has no PrecisePolygon')
        return root

    @classmethod
    def from_xml(cls):
        pass