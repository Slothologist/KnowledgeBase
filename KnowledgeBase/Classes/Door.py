import mongoengine as me
from Room import Room
from Annotation import Annotation


class Door(me.Document):
    roomOne = me.ReferenceField(Room)
    roomTwo = me.ReferenceField(Room)
    annotation = me.EmbeddedDocumentField(Annotation)

    def to_xml(self):
        return ''