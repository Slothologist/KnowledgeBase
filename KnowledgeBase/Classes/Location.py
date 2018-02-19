import mongoengine as me
from Annotation import Annotation
from Room import Room

class Location(me.Document):
    name = me.StringField(max_length=50, unique=True, default='')
    room = me.ReferenceField(Room)
    isBeacon = me.BooleanField(default=False)
    isPlacement = me.BooleanField(default=False)
    annotation = me.EmbeddedDocumentField(Annotation)

    def to_xml(self):
        return ''