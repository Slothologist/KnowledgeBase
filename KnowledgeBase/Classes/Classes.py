
class Person(object):
    def __init__(self, age='0', gender='', shirtcolor='', pose='', gesture=''):
        self.age = age
        self.gender = gender
        self.shirtcolor = shirtcolor
        self.pose = pose
        self.gesture = gesture
        #self.pointcloud TODO


class Room(object):
    def __init__(self, name='', numberOfDoors='0'):
        self.name = name
        self.numberOfDoors = numberOfDoors


class RCObject(object):
    def __init__(self, name='', location='', category='', size='0', shape='', color='', type='', weight='0',
                 graspdifficulty='0', room=''):
        self.name = name
        self.location = location
        self.category = category
        self.size = size
        self.shape = shape
        self.color = color
        self.type = type
        self.weight = weight
        self.graspdifficulty = graspdifficulty
        self.room = room


class Location(object):
    def __init__(self, name='', room='', isBeacon='False', isPlacement='False'):
        self.name = name
        self.room = room
        self.isBeacon = isBeacon
        self.isPlacement = isPlacement

class Door(object):
    def __init__(self, roomOne='', roomTwo=''):
        self.roomOne = roomOne
        self.roomTwo = roomTwo


class Context(object):
    def __init__(self, content='But this is the first question!'):
        self.content = content


class KBase(object):
    def __init__(self, arena=[], crowd=[], context=[], rcobjects=[]):
        self.arena = arena
        self.crowd = crowd
        self.context = context
        self.rcobjects = rcobjects