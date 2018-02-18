from Classes.Classes import RCObjects, Crowd, Context, Arena, Room, Person, Location, Door, RCObject, KBase

#Lists to add your entries to
arena_rooms = []
arena_locations = []
arena_doors = []
objs = []
pers = [] #no person list as those will be hardcoded and properly generated during runtime

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
#wie mit fork, spoon and knife umgehen?
#categorys:
#fruit, container, food, drink, snack, cleaning stuff,
#weitere infos folgen vmtl
objs.append(RCObject(name="apple",          category='fruit', color="red and green",         location=desk, shape="round", size='1'))
objs.append(RCObject(name="bag",            category='container', color="brown",             location=bookshelf, shape="quite flat", size='4'))
objs.append(RCObject(name="banana milk",    category='drink', color="blue and white",        location=kitchencounter, shape="boxy", size='1'))
objs.append(RCObject(name="basket",         category='container', color="green",             location=bookshelf, shape="rectangular", size='4'))
objs.append(RCObject(name="bread",          category='food', color="blue and yellow",        location=stove, shape="bar", size='2'))
objs.append(RCObject(name="cappucino",     category='drink', color="brown",                 location=kitchencounter, shape="cylindrical", size='2'))
objs.append(RCObject(name="cereals",        category='food', color="green and red",          location=stove, shape="boxy", size='2'))
objs.append(RCObject(name="chocolate cookies", category='snack', color="brown",              location=couchtable, shape="boxy", size='2'))
objs.append(RCObject(name="cloth",          category='cleaning stuff', color="yellow green or blue",  location=closet, shape="quite flat", size='4'))
objs.append(RCObject(name="coffeecup",      category='container', color="white and brown",   location=bookshelf, shape="cylindrical", size='2'))
objs.append(RCObject(name="coke",           category='drink', color="red",                   location=kitchencounter, shape="cylindrical", size='2'))
objs.append(RCObject(name="cornflakes",     category='food', color="green white and red",    location=stove, shape="boxy", size='2'))
objs.append(RCObject(name="crackers",       category='food', color="yellow and green",       location=stove, shape="baggy", size='2'))
objs.append(RCObject(name="egg",            category='snack', color="white and red",         location=couchtable, shape="oval", size='0'))
objs.append(RCObject(name="fork",           category='cutlery', color="red blue or green",   location=cabinet, shape="pointy", size='2'))
objs.append(RCObject(name="spoon",          category='cutlery', color="red blue or green",   location=cabinet, shape="elongated", size='2'))
objs.append(RCObject(name="knife",          category='cutlery', color="red blue or green",   location=cabinet, shape="pointy", size='2'))
objs.append(RCObject(name="lemon",          category='fruit', color="yellow",                location=desk, shape="round", size='0'))
objs.append(RCObject(name="noodles",        category='food', color="yellow and black",       location=stove, shape="baggy", size='1'))
objs.append(RCObject(name="orange drink",   category='drink', color="blue and orange",       location=kitchencounter, shape="boxy", size='1'))
objs.append(RCObject(name="paper",          category='cleaning stuff', color="white",        location=closet, shape="cylindrical", size='4'))
objs.append(RCObject(name="paprika",        category='food', color="red yellow or green",    location=stove, shape="round", size='1'))
objs.append(RCObject(name="party cracker",  category='snack', color="red",                   location=couchtable, shape="baggy", size='2'))
objs.append(RCObject(name="pear",           category='fruit', color="green",                 location=desk, shape="oval", size='0'))
objs.append(RCObject(name="peas",           category='food', color="green and black",        location=stove, shape="cylindrical", size='1'))
objs.append(RCObject(name="pepper",         category='food', color="black",                  location=stove, shape="cylindrical", size='0'))
objs.append(RCObject(name="plate",          category='container', color="white",             location=bookshelf, shape="that of a flat bowl", size='4'))
objs.append(RCObject(name="potato",         category='food', color="brown",                  location=stove, shape="potato e", size='0'))
objs.append(RCObject(name="potato soup",    category='food', color="yellow",                 location=stove, shape="boxy", size='2'))
objs.append(RCObject(name="pringles",       category='snack', color="yellow",                location=couchtable, shape="cylindrical", size='4'))
objs.append(RCObject(name="red bowl",       category='container', color="red",               location=bookshelf, shape="that of a deep plate", size='2'))
objs.append(RCObject(name="salt",           category='food', color="black and blue",         location=stove, shape="cylindrical", size='0'))
objs.append(RCObject(name="sponge",         category='cleaning stuff', color="light green",  location=closet, shape="rather boxy", size='0'))
objs.append(RCObject(name="tomato pasta",   category='food', color="red and green",          location=stove, shape="that of a toothpaste tube", size='2'))
objs.append(RCObject(name="towel",          category='cleaning stuff', color="purple",       location=closet, shape="rather flat", size='2'))
objs.append(RCObject(name="water",          category='drink', color="light blue",            location=kitchencounter, shape="cylindrical", size='2'))
objs.append(RCObject(name="white bowl",     category='container', color="white",             location=bookshelf, shape="that af a deep plate", size='2'))

#Crowd-entries
#dummys, overwritten by reportGroup
pers.append(Person(age='3', gender="male", gesture="pointing", pose="sitting", shirtcolor="blue"))
pers.append(Person(age='1', gender="female", gesture="waving", pose="standing", shirtcolor="green"))

#
arena = Arena(rooms=arena_rooms, doors=arena_doors, locations=arena_locations)
crowd = Crowd(persons=pers)
rcobjects = RCObjects(rcobjects=objs)
#context, will use default initializer
context = Context()


kbase = KBase(arena=arena, crowd=crowd, rcobjects=rcobjects, context=context, identifier='TestKBase')

#dump = json.dumps(kbase, cls=ObjectEncoder, indent=2, sort_keys=True)
#print(dump)
#print(json.loads(dump, cls=ObjectDecoder).arena.locations)

import mongoengine as me

db = me.connect('default_db')
db.drop_database('default_db')

#presave documents so that references can be created
for room in arena_rooms:
    room.save()
for location in arena_locations:
    location.save()
for door in arena_doors:
    door.save()
for obj in objs:
    obj.save()
for per in pers:
    per.save()

arena.save()
crowd.save()
context.save()
rcobjects.save()

kbase.save()




