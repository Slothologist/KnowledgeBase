import mongoengine as me


class Person(me.Document):
    age = me.IntField(default=0)
    gender = me.StringField(max_length=20, default='')
    shirtcolor = me.StringField(max_length=20, default='')
    pose = me.StringField(max_length=20, default='')
    gesture = me.StringField(max_length=20, default='')
    #pointcloud


class Crowd(me.Document):
    persons = me.ListField(me.ReferenceField(Person))


class RobotPosition(me.Document):
    label = me.StringField(max_length=100, default='')
    x = me.FloatField(default=0.0)
    y = me.FloatField(default=0.0)
    yaw = me.FloatField(default=0.0)


class PrecisePolygon(me.Document):
    #replace with me.polygon or something like that
    pass


class Annotation(me.Document):
    label = me.StringField(max_length=100, default='')
    polygon = me.ReferenceField(PrecisePolygon)
    viewpoints = me.ListField(me.ReferenceField(RobotPosition))


class Room(me.Document):
    name = me.StringField(max_length=50, unique=True, default='')
    numberOfDoors = me.IntField(default=0)
    annotation = me.ReferenceField(Annotation)


class Location(me.Document):
    name = me.StringField(max_length=50, unique=True, default='')
    room = me.ReferenceField(Room)
    isBeacon = me.BooleanField(default=False)
    isPlacement = me.BooleanField(default=False)
    annotation = me.ReferenceField(Annotation)


class Door(me.Document):
    roomOne = me.ReferenceField(Room)
    roomTwo = me.ReferenceField(Room)
    annotation = me.ReferenceField(Annotation)


class Arena(me.Document):
    locations = me.ListField(me.ReferenceField(Location))
    rooms = me.ListField(me.ReferenceField(Room))
    doors = me.ListField(me.ReferenceField(Door))


class RCObject(me.Document):
    name = me.StringField(max_length=50, unique=True, default='')
    location = me.ReferenceField(Location)
    category = me.StringField(max_length=50, default='')
    shape = me.StringField(max_length=20, default='')
    color = me.StringField(max_length=20, default='')
    type = me.StringField(max_length=20, default='')
    size = me.IntField(default=0)
    weight = me.IntField(default=0)


class RCObjects(me.Document):
    objects = me.ListField(me.ReferenceField(RCObject))


class Context(me.Document):
    lastquestion = me.StringField(max_length=300, default='But this is the first question!')
    content = me.GenericReferenceField(choices=[RCObjects, Person, Room, Location, Door])


class KBase(me.Document):
    identifier = me.StringField(max_length=50, unique=True, default='')
    arena = me.ListField(me.ReferenceField(Arena))
    crowd = me.ListField(me.ReferenceField(Crowd))
    context = me.ListField(me.ReferenceField(Context))
    rcobjects = me.ListField(me.ReferenceField(Person))
