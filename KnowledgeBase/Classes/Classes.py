import mongoengine as me


class RobotPosition(me.EmbeddedDocument):
    label = me.StringField(max_length=100, default='')
    x = me.FloatField(default=0.0)
    y = me.FloatField(default=0.0)
    yaw = me.FloatField(default=0.0)


class Annotation(me.EmbeddedDocument):
    label = me.StringField(max_length=100, default='')
    polygon = me.MultiPointField()
    viewpoints = me.ListField(me.EmbeddedDocumentField(RobotPosition))


class Person(me.Document):
    age = me.IntField(default=0)
    gender = me.StringField(max_length=50, default='')
    shirtcolor = me.StringField(max_length=50, default='')
    pose = me.StringField(max_length=50, default='')
    gesture = me.StringField(max_length=50, default='')
    lastKnownPosition = me.EmbeddedDocumentField(RobotPosition)
    name = me.StringField(max_length=100, default='')
    # pointcloud


class Crowd(me.Document):
    persons = me.ListField(me.ReferenceField(Person))


class Room(me.Document):
    name = me.StringField(max_length=50, unique=True, default='')
    numberOfDoors = me.IntField(default=0)
    annotation = me.EmbeddedDocumentField(Annotation)


class Location(me.Document):
    name = me.StringField(max_length=50, unique=True, default='')
    room = me.ReferenceField(Room)
    isBeacon = me.BooleanField(default=False)
    isPlacement = me.BooleanField(default=False)
    annotation = me.EmbeddedDocumentField(Annotation)


class Door(me.Document):
    roomOne = me.ReferenceField(Room)
    roomTwo = me.ReferenceField(Room)
    annotation = me.EmbeddedDocumentField(Annotation)


class Arena(me.Document):
    locations = me.ListField(me.ReferenceField(Location))
    doors = me.ListField(me.ReferenceField(Door))
    rooms = me.ListField(me.ReferenceField(Room))


class RCObject(me.Document):
    name = me.StringField(max_length=50, unique=True, default='')
    location = me.ReferenceField(Location)
    category = me.StringField(max_length=50, default='')
    shape = me.StringField(max_length=50, default='')
    color = me.StringField(max_length=50, default='')
    type = me.StringField(max_length=50, default='')
    size = me.IntField(default=0)
    weight = me.IntField(default=0)


class RCObjects(me.Document):
    rcobjects = me.ListField(me.ReferenceField(RCObject))


class Context(me.Document):
    lastquestion = me.StringField(max_length=300, default='But this is the first question!')
    content = me.DynamicField(choices=[RCObjects, Person, Room, Location, Door])


class KBase(me.Document):
    identifier = me.StringField(max_length=50, unique=True)
    context = me.ReferenceField(Context)
    crowd = me.ReferenceField(Crowd)
    rcobjects = me.ReferenceField(RCObjects)
    arena = me.ReferenceField(Arena)
