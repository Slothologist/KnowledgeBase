import mongoengine as me


class RobotPosition(me.EmbeddedDocument):
    label = me.StringField(max_length=100, default='')
    x = me.FloatField(default=0.0)
    y = me.FloatField(default=0.0)
    yaw = me.FloatField(default=0.0)

    def to_xml(self):
        return ''