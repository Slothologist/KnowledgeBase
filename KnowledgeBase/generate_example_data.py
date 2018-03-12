from Classes import *
import mongoengine as me
from utils import save_complete_db, add_annotation
import xml.etree.ElementTree as ET
from xml.dom import minidom

import sys



#Lists to add your entries to
arena_rooms = []
arena_locations = []
arena_doors = []
objs = []
pers = []


# load annotation file. general stuff (argument handling etc)
args = sys.argv
if len(args) < 3:
    print('Usage: python generate_example_data.py <DatabaseName> <AnnotationFile>')
    sys.exit()

db = me.connect(args[1], host="127.0.0.1", port=27018)
db.drop_database(args[1])

inputstr = ''

with open(args[2], 'r') as f:
    inputstr = f.read()

annotations = [] # list where the xml annotations will be saved

#add those annotations to the list
annotationTree = ET.fromstring(inputstr)
for annotation in annotationTree.getchildren():
    if annotation.tag == 'ANNOTATION':
        annotations.append(annotation)

##################################################################################################################################################################

##Data which shall be put into the database
## Modifiy at will

#Arena-entries (locations, rooms etc)
#<N_placementTwo> = (dinner table) | cabinet | bookshelf | (kitchen counter) | sofa | (couch table) | (side table) | (stove) | bed | closet | desk | bar;
diningroom = Room(name='diningroom', numberOfDoors='2')
dinnertable = Location(name='dinnertable', room=diningroom, isBeacon='True')
closet = Location(name='closet', room=diningroom, isBeacon='True')
desk = Location(name='desk', room=diningroom, isPlacement='True')
arena_rooms.append(diningroom)
arena_locations.append(dinnertable)
arena_locations.append(closet)
arena_locations.append(desk)

livingroom = Room(name='livingroom', numberOfDoors='0')
couchtable = Location(name='couchtable', room=livingroom)
sofa = Location(name='sofa', room=livingroom)
bar = Location(name='bar', room=livingroom)
cabinet = Location(name='cabinet', room=livingroom)
arena_rooms.append(livingroom)
arena_locations.append(couchtable)
arena_locations.append(sofa)
arena_locations.append(bar)
arena_locations.append(cabinet)

kitchen = Room(name='kitchen', numberOfDoors='0')
bookshelf = Location(name='bookshelf', room=kitchen)
kitchencounter = Location(name='kitchencounter', room=kitchen)
stove = Location(name='stove', room=kitchen)
arena_rooms.append(kitchen)
arena_locations.append(bookshelf)
arena_locations.append(kitchencounter)
arena_locations.append(stove)

bedroom = Room(name='bedroom', numberOfDoors='1')
bed = Location(name='bed', room=bedroom)
sidetable = Location(name='sidetable', room=bedroom)
arena_rooms.append(bedroom)
arena_locations.append(bed)
arena_locations.append(sidetable)

outside = Room(name='outside', numberOfDoors='0')
arena_rooms.append(outside)#if you have doors to the outside it would make sense to also annotate an extra room for the outside

arena_doors.append(Door(roomOne=outside, roomTwo=bedroom))
arena_doors.append(Door(roomOne=diningroom, roomTwo=outside))

#Objects-Entries
#categorys:
#fruit, container, food, drink, snack, cleaning stuff,
objs.append(Rcobject(name="apple",          category='fruit', color="red and green",         location=desk, shape="round", size='1'))
objs.append(Rcobject(name="bag",            category='container', color="brown",             location=bookshelf, shape="quite flat", size='4'))
objs.append(Rcobject(name="banana milk",    category='drink', color="blue and white",        location=kitchencounter, shape="boxy", size='1'))
objs.append(Rcobject(name="basket",         category='container', color="green",             location=bookshelf, shape="rectangular", size='4'))
objs.append(Rcobject(name="bread",          category='food', color="blue and yellow",        location=stove, shape="bar", size='2'))
objs.append(Rcobject(name="cappucino",     category='drink', color="brown",                 location=kitchencounter, shape="cylindrical", size='2'))
objs.append(Rcobject(name="cereals",        category='food', color="green and red",          location=stove, shape="boxy", size='2'))
objs.append(Rcobject(name="chocolate cookies", category='snack', color="brown",              location=couchtable, shape="boxy", size='2'))
objs.append(Rcobject(name="cloth",          category='cleaning stuff', color="yellow green or blue",  location=closet, shape="quite flat", size='4'))
objs.append(Rcobject(name="coffeecup",      category='container', color="white and brown",   location=bookshelf, shape="cylindrical", size='2'))
objs.append(Rcobject(name="coke",           category='drink', color="red",                   location=kitchencounter, shape="cylindrical", size='2'))
objs.append(Rcobject(name="cornflakes",     category='food', color="green white and red",    location=stove, shape="boxy", size='2'))
objs.append(Rcobject(name="crackers",       category='food', color="yellow and green",       location=stove, shape="baggy", size='2'))
objs.append(Rcobject(name="egg",            category='snack', color="white and red",         location=couchtable, shape="oval", size='0'))
objs.append(Rcobject(name="fork",           category='cutlery', color="red blue or green",   location=cabinet, shape="pointy", size='2'))
objs.append(Rcobject(name="spoon",          category='cutlery', color="red blue or green",   location=cabinet, shape="elongated", size='2'))
objs.append(Rcobject(name="knife",          category='cutlery', color="red blue or green",   location=cabinet, shape="pointy", size='2'))
objs.append(Rcobject(name="lemon",          category='fruit', color="yellow",                location=desk, shape="round", size='0'))
objs.append(Rcobject(name="noodles",        category='food', color="yellow and black",       location=stove, shape="baggy", size='1'))
objs.append(Rcobject(name="orange drink",   category='drink', color="blue and orange",       location=kitchencounter, shape="boxy", size='1'))
objs.append(Rcobject(name="paper",          category='cleaning stuff', color="white",        location=closet, shape="cylindrical", size='4'))
objs.append(Rcobject(name="paprika",        category='food', color="red yellow or green",    location=stove, shape="round", size='1'))
objs.append(Rcobject(name="party cracker",  category='snack', color="red",                   location=couchtable, shape="baggy", size='2'))
objs.append(Rcobject(name="pear",           category='fruit', color="green",                 location=desk, shape="oval", size='0'))
objs.append(Rcobject(name="peas",           category='food', color="green and black",        location=stove, shape="cylindrical", size='1'))
objs.append(Rcobject(name="pepper",         category='food', color="black",                  location=stove, shape="cylindrical", size='0'))
objs.append(Rcobject(name="plate",          category='container', color="white",             location=bookshelf, shape="that of a flat bowl", size='4'))
objs.append(Rcobject(name="potato",         category='food', color="brown",                  location=stove, shape="potato e", size='0'))
objs.append(Rcobject(name="potato soup",    category='food', color="yellow",                 location=stove, shape="boxy", size='2'))
objs.append(Rcobject(name="pringles",       category='snack', color="yellow",                location=couchtable, shape="cylindrical", size='4'))
objs.append(Rcobject(name="red bowl",       category='container', color="red",               location=bookshelf, shape="that of a deep plate", size='2'))
objs.append(Rcobject(name="salt",           category='food', color="black and blue",         location=stove, shape="cylindrical", size='0'))
objs.append(Rcobject(name="sponge",         category='cleaning stuff', color="light green",  location=closet, shape="rather boxy", size='0'))
objs.append(Rcobject(name="tomato pasta",   category='food', color="red and green",          location=stove, shape="that of a toothpaste tube", size='2'))
objs.append(Rcobject(name="towel",          category='cleaning stuff', color="purple",       location=closet, shape="rather flat", size='2'))
objs.append(Rcobject(name="water",          category='drink', color="light blue",            location=kitchencounter, shape="cylindrical", size='2'))
objs.append(Rcobject(name="white bowl",     category='container', color="white",             location=bookshelf, shape="that of a deep plate", size='2'))

#Crowd-entries
#dummys, overwritten by reportGroup
pers.append(Person(name='michael',
                   uuid='1',
                   agefrom='3',
                   ageto='5',
                   gender="male",
                   gesture="pointing",
                   posture="sitting",
                   shirtcolor="blue",
                   faceid=-1,
                   position=Positiondata(theta=1.1, frameid="map", point2d=Point2d(x=1.2, y=3.4))))
pers.append(Person(name='noah',
                   uuid='0',
                   agefrom='3',
                   ageto='5',
                   gender="female",
                   gesture="waving",
                   posture="standing",
                   shirtcolor="green",
                   faceid=-1,
                   position=Positiondata(theta=1.9, frameid="map", point2d=Point2d(x=5.6, y=7.8))))

######################################################################################################################

#match read annotations to rooms, locations and doors

arena_rooms = [add_annotation(x, annotations) for x in arena_rooms]
arena_doors = [add_annotation(x, annotations) for x in arena_doors]
arena_locations = [add_annotation(x, annotations) for x in arena_locations]

#
arena = Arena(rooms=arena_rooms, doors=arena_doors, locations=arena_locations)
crowd = Crowd(persons=pers)
rcobjects = Rcobjects(rcobjects=objs)

kbase = Kbase(arena=arena, crowd=crowd, rcobjects=rcobjects, identifier='TestKBase')

#dump = json.dumps(kbase, cls=ObjectEncoder, indent=2, sort_keys=True)
#print(dump)
#print(json.loads(dump, cls=ObjectDecoder).arena.locations)

#print('DEBUG: toxml ')
bla = kbase.to_xml()
#print(minidom.parseString(ET.tostring(kbase.to_xml(), encoding='utf-8')).toprettyxml(indent="   "))

save_complete_db(kbase)
exit(0)