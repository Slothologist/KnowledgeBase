import mongoengine as me
from Person import Person


class Crowd(me.Document):
    persons = me.ListField(me.ReferenceField(Person))

    def to_xml(self):
        return ''