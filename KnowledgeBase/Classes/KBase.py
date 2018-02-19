import mongoengine as me
from Context import Context
from Crowd import Crowd
from RCObjects import RCObjects
from Arena import Arena


class KBase(me.Document):
    identifier = me.StringField(max_length=50, unique=True)
    context = me.ReferenceField(Context)
    crowd = me.ReferenceField(Crowd)
    rcobjects = me.ReferenceField(RCObjects)
    arena = me.ReferenceField(Arena)

    def to_xml(self):
        return ''