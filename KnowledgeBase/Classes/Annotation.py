import mongoengine as me
from RobotPosition import RobotPosition


class Annotation(me.EmbeddedDocument):
    label = me.StringField(max_length=100, default='')
    polygon = me.MultiPointField()
    viewpoints = me.ListField(me.EmbeddedDocumentField(RobotPosition))

    def to_xml(self):
        return ''