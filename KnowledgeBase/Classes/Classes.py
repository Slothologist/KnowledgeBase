import json
import inspect


class Person():
    def __init__(self, age='0', gender='', shirtcolor='', pose='', gesture=''):
        self.age = age
        self.gender = gender
        self.shirtcolor = shirtcolor
        self.pose = pose
        self.gesture = gesture
        #self.pointcloud TODO


class Room():
    def __init__(self, name='', numberOfDoors='0'):
        self.name = name
        self.numberOfDoors = numberOfDoors


class RCObject():
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


class Location():
    def __init__(self, name='', room='', isBeacon='False', isPlacement='False'):
        self.name = name
        self.room = room
        self.isBeacon = isBeacon
        self.isPlacement = isPlacement


class Door():
    def __init__(self, roomOne='', roomTwo=''):
        self.roomOne = roomOne
        self.roomTwo = roomTwo


class Context():
    def __init__(self, content='But this is the first question!'):
        self.content = content


class Arena():
    def __init__(self, rooms=[], locations=[], doors=[]):
        self.locations = locations
        self.rooms = rooms
        self.doors = doors


class Crowd():
    def __init__(self, persons=[]):
        self.persons = persons


class RCObjects():
    def __init__(self, objects=[]):
        self.objects = objects


class Annotation():
    pass


class Point2D():
    pass


class PrecisePolygon():
    pass


class RobotPosition():
    pass

class KBase():
    def __init__(self, arena=Arena(), crowd=Crowd(), context=Context(), rcobjects=RCObjects(), identifier=''):
        self.arena = arena
        self.crowd = crowd
        self.context = context
        self.rcobjects = rcobjects
        self.identifier = identifier


class ObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "to_json"):
            return self.default(obj.to_json())
        elif hasattr(obj, "__dict__"):
            d = dict(
                (key, value)
                for key, value in inspect.getmembers(obj)
                if not key.startswith("__")
                and not inspect.isabstract(value)
                and not inspect.isbuiltin(value)
                and not inspect.isfunction(value)
                and not inspect.isgenerator(value)
                and not inspect.isgeneratorfunction(value)
                and not inspect.ismethod(value)
                and not inspect.ismethoddescriptor(value)
                and not inspect.isroutine(value)
            )
            d['python_class_name'] = obj.__class__.__name__
            return self.default(d)
        return obj


class ObjectDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        if 'python_class_name' not in obj:
            return obj
        python_class_str = obj.pop('python_class_name')
        get_python_class = lambda x: globals()[x]
        python_class = get_python_class(python_class_str)
        python_obj = python_class(**obj)
        return python_obj