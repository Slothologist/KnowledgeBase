import mongoengine as me
from RobotPosition import RobotPosition


class Person(me.Document):
    age = me.IntField(default=0)
    gender = me.StringField(max_length=50, default='')
    shirtcolor = me.StringField(max_length=50, default='')
    pose = me.StringField(max_length=50, default='')
    gesture = me.StringField(max_length=50, default='')
    lastKnownPosition = me.EmbeddedDocumentField(RobotPosition)
    name = me.StringField(max_length=100, default='')
    # pointcloud

    def to_xml(self):
        return ''