import mongoengine as me
from Room import Room
from Location import Location
from Door import Door



class Arena(me.Document):
    locations = me.ListField(me.ReferenceField(Location))
    doors = me.ListField(me.ReferenceField(Door))
    rooms = me.ListField(me.ReferenceField(Room))

    def to_xml(self):
        return ''