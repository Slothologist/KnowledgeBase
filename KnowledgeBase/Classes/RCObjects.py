import mongoengine as me
from RCObject import RCObject


class RCObjects(me.Document):
    rcobjects = me.ListField(me.ReferenceField(RCObject))

    def to_xml(self):
        return ''