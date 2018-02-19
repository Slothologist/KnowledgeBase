import mongoengine as me
from Annotation import Annotation


class Room(me.Document):
    name = me.StringField(max_length=50, unique=True, default='')
    numberOfDoors = me.IntField(default=0)
    annotation = me.EmbeddedDocumentField(Annotation)

    def to_xml(self):
        return ''